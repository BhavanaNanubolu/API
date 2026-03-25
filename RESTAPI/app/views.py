from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Travels
from .serializer import TravelSerializer
from rest_framework import status
# Create your views here.
@api_view(['get','post'])
def index(request):
    if request.method == "GET":
        a = Travels.objects.all()
        serail =TravelSerializer(a,many = True)
        return Response(serail.data)
    elif request.method  == "POST":
        a = TravelSerializer(data = request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)
        
@api_view(['get','put','delete'])
def update(request,id):
    try:
        a = Travels.objects.get(id = id)
    except Exception as e:
        return Response(e)
    if a:
        if request.method == "GET":
            serail = TravelSerializer(a)
            return Response(serail.data)
        if request.method == "PUT":
            b = TravelSerializer(instance = a ,data = request.data)
            if b.is_valid():
                b.save()
                return Response(b.data,status= status.HTTP_200_OK)        

            else:
                return Response(status=status.HTTP_304_NOT_MODIFIED)
        elif request.method == "DELETE":
            a.delete()
            return Response(status=status.HTTP_200_OK)


