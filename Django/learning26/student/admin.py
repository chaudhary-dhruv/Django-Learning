from django.contrib import admin
from .models import Student,Product,StudentProfile
# Register your models here.

admin.site.register(Student) 
admin.site.register(Product)
admin.site.register(StudentProfile)
