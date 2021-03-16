from django.shortcuts import render
from recommendation.models import Recommendation

# Create your views here.
def recommend(request):
    recommendation=Recommendation.objects.all()
    return render(request,'recommendation/recommend.html',{'recommendation':recommendation})
