import datetime
from decimal import Decimal
from django.db import models
from datetime import date
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class items(models.Model):
    id = models.AutoField(primary_key=True)
    itemcode = models.CharField(max_length=45, unique=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=85)
    brand = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    unit = models.CharField(max_length=45)              
    qty = models.FloatField(null=True, blank=True, default=0)     
    price =models.FloatField(null=True, blank=True, default=0) #models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    saleprice =models.FloatField(null=True, blank=True, default=0) #models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    pricingbyID = models.CharField(max_length=45)       
    pricingdate = models.DateTimeField(auto_now=True)
    active = models.PositiveSmallIntegerField(default=1, null=True)           
    class Meta:
        db_table = "items"


class itemserials(models.Model):
    id = models.AutoField(primary_key=True)
    itemcode = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=85)
    brand = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    unit = models.CharField(max_length=45)          
    qty = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])             
    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    saleprice = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    pricingbyID = models.CharField(max_length=45)       
    pricingdate =  models.DateTimeField(auto_now=True)         
    class Meta:
        db_table = "itemserials"


class itemserials_details(models.Model):
    id = models.AutoField(primary_key=True)
    itemcode = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=85)
    brand = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    unit = models.CharField(max_length=45)          
    qty = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])             
    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    saleprice = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    pricingbyID = models.CharField(max_length=45)       
    pricingdate =  models.DateTimeField(auto_now=True)         
    class Meta:
        db_table = "itemserials_details"
        

