from django.db import models

# Create your models here.
class Foodsales(models.Model):
    OrderDate=models.CharField(max_length=30,null=True)
    Region=models.CharField(max_length=30,null=True)
    City=models.CharField(max_length=30,null=True)
    Category=models.CharField(max_length=30,null=True)
    Product=models.CharField(max_length=30,null=True)
    Quantity=models.CharField(max_length=30,null=True)
    UnitPrice=models.CharField(max_length=30,null=True)



