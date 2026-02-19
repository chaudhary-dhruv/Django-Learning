from django.shortcuts import render, HttpResponse
from .models import Service
from .forms import ServiceForm

# Create your views here.

def serviceList(request):
    services = Service.objects.all().values()
    return render(request , 'service/serviceList.html' ,{'services':services})

def createServiceForm(request):
    print(request.method)
    if request.method == "POST":
        form = ServiceForm(request.POST)
        form.save()
        return HttpResponse("Form Created Sucessfully...")
    else:
        form = ServiceForm()
        return render(request , "service/createServiceForm.html" , {"form" : form})

