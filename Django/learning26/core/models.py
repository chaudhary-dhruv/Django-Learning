from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    roleChoice = (
        ('admin' , 'admin'),
        ('faculty' , 'faculty'),
        ('student' , 'student')
    ) 

    role =  models.CharField(max_length=100 , choices=roleChoice , null=True , blank= True)


    
