from django.shortcuts import render

# Create your views here.

def studentHome(request):
    return render(request,"studentTemplate/studentHome.html")
def studentDashboard(request):
    student = {"name":"raj","age":23,"city":"Ahmedabad"}
    return render(request,"studentTemplate/dashboard.html",student)    
    #student/studentDashboard.html
    #folder/filename