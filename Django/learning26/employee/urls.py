from django.urls import path
from django.urls import include
from . import views

urlpatterns=[
    path('employeeFilter/' , views.employeefilter),
    path('employeeList/' , views.employeelist , name='employeeList'),
    path('employeeCreate/' , views.employeeCreate , name='employeeCreate'),
    path('deleteEmployee/<int:id>' , views.deleteEmployee , name='deleteEmployee'),
    path('filterEmployee/' , views.filterEmployee , name='filterEmployee'),
    path('sortEmployee/<int:id>' , views.sortEmployee , name='sortEmployee' ),
    path('updateEmployee/<int:id>' , views.employeeUpdate , name='updateEmployee'),
    path('home/' , views.home , name='home')
]