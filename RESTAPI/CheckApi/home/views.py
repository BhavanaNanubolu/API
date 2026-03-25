from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    data = requests.get("http://127.0.0.1:8000/").json()
    context = {
        'data':data
    }
    return render(request,'index.html',context)
