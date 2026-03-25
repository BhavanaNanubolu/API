from django.shortcuts import render
import requests
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def index(request):
    data="" 
    context={}
    if request.method=="POST":
        city=request.POST.get('city')
        data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.API_KEY}").json()
        context={'data':data}
    return render(request,'index.html',context)

