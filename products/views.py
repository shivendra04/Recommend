from django.shortcuts import render,redirect,HttpResponse
from products.models import Product
from user.models import User
from recommendation.models import Recommendation
from . forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.

def view_list(request):
    product = Product.objects.all()

    paginator = Paginator(product, 15)
    page_number = request.GET.get('page')

    try:
        productlist = paginator.page(page_number)
    except PageNotAnInteger:
	    productlist = paginator.page(1)
    except EmptyPage:
	     productlist = paginator.page(paginator.num_pages)

    return render(request,'products/productlist.html',{'productlist':productlist})

@login_required
def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productview')
    return render(request,'products/add.html',{'form':form})

@login_required
def update_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('/productview')
    return render(request,'products/productupdate.html',{'product':product})

@login_required
def product_search(request):
    query = request.GET['query']
    products = Product.objects.filter(size__icontains = query)|Product.objects.filter(shape__icontains=query)

    cur_user = request.user.id
    search_data = products.values('Pid')

    recomends = Recommendation.objects.filter(User_id__iexact=cur_user)
    recomend_data = recomends.values('Product_id')
    Pid=[]
    for data in recomend_data:
        Pid.append(data['Product_id'])

    for entry in search_data:
        if entry['Pid'] not in Pid:
            Recommendation(User_id = cur_user,Product_id = entry['Pid']).save()

    return render(request,'products/search.html',{'product':products})
