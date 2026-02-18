from django.urls import path
from django.urls import include
from . import views

urlpatterns=[
    path('employeeFilter/' , views.employeefilter),
    path('employeeList/' , views.employeelist)
]