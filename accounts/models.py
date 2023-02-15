from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from employee.models import Employee


class Account(models.Model):
    accountname = models.CharField(max_length=100,blank=True, null= True)
    accountid = models.IntegerField(blank=True, null= True)
    birthdate = models.DateField(default=datetime.now,blank=True, null= True)
    phone = models.CharField(max_length=20,blank=True, null= True)
    registration_date= models.DateField(default=datetime.now,blank=True, null= True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',default='MaskGroup1.png',blank = True, null= True)
    total_balance = models.IntegerField(blank=True, null= True)
    total_profit = models.IntegerField(blank=True, null= True)
    total_trades = models.IntegerField(blank=True, null= True)
    new_trades = models.IntegerField(blank=True, null= True)
    balance = models.IntegerField(blank=True, null= True)
    remaining_days = models.IntegerField(blank=True, null= True)
    leverage = models.CharField(max_length=10,blank=True, null= True)
    percentage_in_trade = models.IntegerField(blank=True, null= True)
    equity_percentage = models.IntegerField(blank=True, null= True)
    title = models.CharField(max_length=100,blank=True, null= True)
    country = models.CharField(max_length=100,blank=True, null= True)
    language = models.CharField(max_length=100,blank=True, null= True)
    contractname = models.CharField(max_length=100,default="A",blank=True, null= True)

    def __str__(self):
        return self.accountname

