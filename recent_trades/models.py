from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account




class Recent_Trades(models.Model):
    account = models.ForeignKey(Account, on_delete= models.CASCADE)
    pair = models.CharField(max_length=20)
    coef = models.DecimalField(max_digits=2, decimal_places=1)
    portion = models.CharField(max_length=50)
    type  = models.CharField(max_length=4 , choices= [('Buy' , 'Buy'),('Sell' , 'Sell')]) 
    

    def __str__(self):
        return self.account.accountname
