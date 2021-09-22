import datetime
from decimal import Decimal
from django.db import models
from datetime import date
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class items(models.Model):
    id = models.AutoField(primary_key=True)
    itemcode = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=85)
    brand = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    unit = models.CharField(max_length=45)          # meter count
    qty = models.FloatField(default=0)              # meter count
    price = models.FloatField(default=0) 
    saleprice = models.FloatField(default=0) 
    pricingbyID = models.CharField(max_length=45)       # meter count
    pricingdate = models.DateField(("Date"))          # meter count
    class Meta:
        db_table = "items"


class itemserials(models.Model):
    id = models.AutoField(primary_key=True)
    itemcode = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=85)
    brand = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    unit = models.CharField(max_length=45)          # meter count
    qty = models.FloatField(default=0)              # meter count
    price = models.FloatField(default=0) 
    saleprice = models.FloatField(default=0) 
    pricingbyID = models.CharField(max_length=45)       # meter count
    pricingdate = models.DateField(("Date"))          # meter count

    class Meta:
        db_table = "itemserials"


class itemserials_details(models.Model):
    id = models.AutoField(primary_key=True)
    itemcode = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=85)
    brand = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    unit = models.CharField(max_length=45)          # meter count
    qty = models.FloatField(default=0)              # meter count
    price = models.FloatField(default=0) 
    saleprice = models.FloatField(default=0) 
    pricingbyID = models.CharField(max_length=45)       # meter count
    pricingdate = models.DateField(("Date"))          # meter count

    class Meta:
        db_table = "itemserials_details"
        

