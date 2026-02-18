from django.shortcuts import render
from .models import Service

# Create your views here.

def serviceList(request):
    services = Service.objects.all().values()
    return render(request , 'service/serviceList.html' ,{'services':services})
