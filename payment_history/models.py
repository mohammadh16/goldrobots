from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account



class Payment_history(models.Model):
    account = models.ForeignKey(Account, on_delete= models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()
    type  = models.CharField(max_length=10 , choices= [('Deposit' , 'Deposit'),('Withdraw' , 'Withdraw')])
    status  = models.CharField(max_length=10 , choices= [('Success' , 'Success'),('Fail' , 'Fail')]) 
    via = models.CharField(max_length=50)
    amount = models.IntegerField()


    
    def __str__(self):
        return self.account.accountname