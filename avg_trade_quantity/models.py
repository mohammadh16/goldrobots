from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account




class Avg_trade_quantity(models.Model):
    account = models.ForeignKey(Account, on_delete= models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.account.accountname
