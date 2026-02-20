from django.shortcuts import render,redirect
from .forms import userForm
from .models import User

# Create your views here.

def registerUser(request):
    if request.method == "POST":
        form = userForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('employeeList')
        
    else:
        form = userForm()
        return render(request , 'core/register.html' , {"form" : form})

