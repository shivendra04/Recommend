from django.shortcuts import render,redirect
from user.models import User
from . forms import UserForm,SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def view_list(request):
    user=User.objects.all()
    return render(request,'user/userlist.html',{'user':user})

def add_user(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view')
    return render(request,'user/add.html',{'form':form})

def update_user(request,id):
    user=User.objects.get(id=id)
    if request.method=='POST':
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('/view')
    return render(request,'user/userupdate.html',{'user':user})

def logout_view(request):
    return render(request,'user/logout.html')

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        #if form.is_valid():
        #    form.save()
        user=form.save()
        user.set_password(user.password)
        user.save()
        #form.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'user/signup.html',{'form':form})
