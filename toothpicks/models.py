from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
# Create your models here.
class product(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    price=models.CharField(max_length=30)
    img = models.TextField() 
    def __str__(self):
        return f"Product NO {self.sno} - {self.name}"
class Contacst(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    message=models.CharField(max_length=255)
    def __str__(self):
        return f"Contact No {self.sno} - {self.name}- {timezone.now()}"
class Order(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    number=models.CharField(max_length=255)
    product=models.CharField(max_length=55)
    quantity=models.CharField(max_length=55)  
    message=models.TextField(max_length=255)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return f"Order No {self.sno} - {self.name}- {timezone.now()}"