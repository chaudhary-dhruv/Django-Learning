from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Hello")

def aboutUs(request):
    return render(request , 'aboutus.html')

def contactUs(request):
    return render(request , 'contactus.html')

def home(request):
    return render(request , 'home.html')