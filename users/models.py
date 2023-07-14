from django.db import models

# Create your models here.

# Creating Company Model

class Company(models.Model):
    choice=(('IT','IT'),('NON IT','NON IT'),('Mobile','Mobile'))
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=choice)
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return (self.name+"-->"+self.location)
    
    
#Create Class Employee


class Employee(models.Model):
    choice=(('IT Developer','Developer'),('IT Engineer','Engineer'),('Manager','Manager'),('HR','HR'))
    name=models.CharField(max_length=50)
    email=models.EmailField()
    about=models.TextField()
    active_employee=models.BooleanField(default=True)
    address=models.TextField()
    phone=models.CharField(max_length=10)
    position=models.CharField(max_length=50,choices=choice)
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE)

    
    
    
    