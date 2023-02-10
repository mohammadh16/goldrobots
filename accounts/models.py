from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from employee.models import Employee


class Account(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.DO_NOTHING)
    accountname = models.CharField(max_length=100)
    accountid = models.IntegerField()
    birthdate = models.DateField(default=datetime.now)
    phone = models.CharField(max_length=20)
    registration_date= models.DateField(default=datetime.now)
    email = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank = True)
    total_balance = models.IntegerField()
    total_profit = models.IntegerField()
    total_trades = models.IntegerField()
    new_trades = models.IntegerField()
    balance = models.IntegerField()
    remaining_days = models.IntegerField()
    leverage = models.CharField(max_length=10)
    percentage_in_trade = models.IntegerField()
    equity_percentage = models.IntegerField()

    def __str__(self):
        return self.accountname

