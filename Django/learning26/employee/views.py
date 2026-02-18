from django.shortcuts import render
from .models import Employee


# Create your views here.

def employeelist(request):
    #employees = Employee.objects.all()    # select * from employee
    employees = Employee.objects.all().values()
    print(employees)
    return render(request , 'employee/employeeList.html' , {"employees" : employees})

def employeefilter(request):
    employee = Employee.objects.filter(name = 'Dhruv').values()
    employee2 = Employee.objects.filter(post = "Designer").values()
    employee3 = Employee.objects.filter(name= "Dhruv" , post = "Designer").values()


    employee4 = Employee.objects.filter(age__gt=23).values()
    employee5 = Employee.objects.filter(age__gte=23).values()

    employee6 = Employee.objects.filter(post__exact="Writer").values()
    employee7 = Employee.objects.filter(post__iexact="writer").values()

    employee8 = Employee.objects.filter(name__contains="r").values()
    employee9 = Employee.objects.filter(name__icontains="R").values()

    employee10 = Employee.objects.filter(name__startswith="D").values()
    employee11 = Employee.objects.filter(name__endswith="R").values()
    employee12 = Employee.objects.filter(name__istartswith="d").values()
    employee13 = Employee.objects.filter(name__iendswith="R").values()

    employee14 = Employee.objects.filter(name__in = ['Gopi','Komal']).values()

    employee15 = Employee.objects.filter(age__range = [20,25]).values()

    employee16 = Employee.objects.order_by("age").values()     #asc
    employee17 = Employee.objects.order_by("-age").values()    #desc

    employee18 = Employee.objects.order_by("-salary").values()



    print("Query 1 :" , employee)
    print("Query 2 :" , employee2)
    print("Query 3 :" , employee3)
    print("Query 4 :" , employee4)
    print("Query 5 :" , employee5)
    print("Query 6 :" , employee6)
    print("Query 7: " , employee7)
    print("Query 8: " , employee8)
    print("Query 9: " , employee9)
    print("Query 10: " , employee10)
    print("Query 11: " , employee11)
    print("Query 12: " , employee12)
    print("Query 13: " , employee13)
    print("Query 14: " , employee14)
    print("Query 15: " , employee15)
    print("Query 16: " , employee16)
    print("Query 17: " , employee17)
    print("Query 18 :" , employee18)
    

    return render(request , 'employee/employeeFilter.html')
