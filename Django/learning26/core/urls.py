from django.urls import path
from . import views

urlpatterns =[
    path('SignIn/' , views.registerUser)
]