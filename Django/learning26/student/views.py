from django.shortcuts import render

def home(request):
    return render(request , 'student.html')

def dashboard(request):
    student = {
        "name" : "Dhruv" ,
        "age" : 25 , 
        "sport" : "Cricket"
    }
    return render(request , 'studentTemplate/dashboard.html',student)
