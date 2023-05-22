from django.db import models
from datetime import date

# Create your models here.


class Product(models.Model):
    pname = models.CharField(max_length=50,null=False)
    
    
    
class products(models.Model): 
    pname = models.CharField(max_length=50)
    party1 = models.CharField(max_length=50)
    party2 = models.CharField(max_length=50)
    party3 = models.CharField(max_length=50)
    party4 = models.CharField(max_length=50)
    p1_imp = models.BooleanField(default=False)
    p2_imp = models.BooleanField(default=False)
    p3_imp = models.BooleanField(default=False)
    p4_imp = models.BooleanField(default=False)
    


class user_data(models.Model): 
    username = models.CharField(max_length=100) 
    password = models.CharField(max_length=50)
    
    
class short(models.Model):
    pname = models.ForeignKey(products,on_delete=models.CASCADE)
    qty = models.CharField(max_length=20)
    status = models.CharField(max_length=20,default="pending")
    ordate = models.DateField(blank=True,null=True)
    is_emergancy = models.BooleanField(default=False)
    

class exp(models.Model):
    pname = models.ForeignKey(products,on_delete=models.CASCADE)
    batch = models.CharField(max_length=20)
    qty = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    party = models.CharField(max_length=20,default="None")
    status = models.CharField(max_length=20,default="pending")