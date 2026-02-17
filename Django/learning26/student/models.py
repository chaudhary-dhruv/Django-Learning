from django.db import models

# Create your models here.
class Student(models.Model):
    studentName= models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)

    #meta class
    class Meta:
        db_table = "student" #table name
    def __str__(self):
        return self.studentName
    
class Product(models.Model):
    productName = models.CharField(max_length=50)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "product"
    def __str__(self):
        return self.productName
    
class StudentProfile(models.Model):
    hobbies = (("Reading" , "Reading"),
               ("Travel" , "Travel"),
               ("Music" , "Music"))
    gender = (("Male" , "Male"),
              ("female" , "Feamle"))
    studentId = models.OneToOneField(Student , on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100 , choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10 , choices=gender)
    studentDOB = models.DateField()

    class Meta:
        db_table = "studentprofile"

    def __str__(self):
        return self.studentId.studentName
    
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryName    

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName 

    