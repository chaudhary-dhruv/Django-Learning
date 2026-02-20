from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('serviceList/' , views.serviceList),
    path('createServiceForm/' , views.createServiceForm )
]