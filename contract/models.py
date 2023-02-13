from django.db import models
from accounts.models import Account 

class Contract(models.Model):
    name = models.CharField(max_length=10 , choices= [('A' , 'A'),('B' , 'B'),('C' , 'C'),('D' , 'D')], blank=True)
    minimum_duration = models.IntegerField(blank=True)
    minimum_deposit = models.IntegerField( blank=True)
    garantie_percentage = models.IntegerField( blank=True)
    admin_clients = models.IntegerField( blank=True)
    level = models.CharField( max_length=50, blank=True)
    leverage = models.CharField( max_length=200, choices= [('' , ''),('1:100' , '1:100'),('1:200' , '1:200'),('1:500' , '1:500'),('1:1000' , '1:1000')], blank=True)
    trading_timeframe = models.CharField( max_length=200,choices= [('1 min' , '1 min'),('5 mins' , '5 mins'),('15 mins' , '15 mins'),('1 hour' , '1 hour'),('1 day' , '1 day'),('all timeframe' , 'all timeframe')], blank=True)
    max_usage_percentage = models.CharField( max_length=200,choices= [('35%' , '35%'),('50%' , '50%'),('85%' , '85%'),('100%' , '100%')], blank=True)
    add_extra_days = models.CharField( max_length=200,choices= [('5 days' , '5 days'),('10 days' , '10 days'),('25 days' , '25 days'),('50 days' , '50 days')], blank=True)
    time_range = models.CharField( max_length=200,choices= [('London ' , 'London '),('Tokyo' , 'Tokyo'),('New York' , 'New York')], blank=True)
    first_point_ruler = models.IntegerField(default= 5,blank=True)
    second_point_ruler = models.IntegerField(default= 10,blank=True)
    third_point_ruler = models.IntegerField(default= 15,blank=True)
    fourth_point_ruler = models.IntegerField(default= 20,blank=True)
    bulima_share = models.CharField(max_length=50, default= "40",blank=True)
    client_share = models.CharField(max_length=50, default= "60",blank=True)
    


    def __str__(self):
        return self.name

    


