from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class contact(models.Model):
    email = models.EmailField()
    Name = models.CharField(max_length=30)
    dese = models.TextField(max_length=500)
    Phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.Name


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    catagory = models.CharField(max_length=30,default="")
    prise = models.IntegerField(default=0)
    dese = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/image")
    
    def __str__(self) -> str:
        return self.product_name
    
    

class order(models.Model):
    id = models.AutoField(primary_key= True)
    item = models.CharField(max_length=1000)
    email = models.EmailField()
    Name = models.CharField(max_length=30)
    address = models.TextField(max_length=500)
    Phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.Name