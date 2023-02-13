from django.db import models
from datetime import datetime


class Employee(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField()
    email = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')


    def __str__(self):
        return self.name

    def setemail(self):
        self.email="mailto:"+ str(self.email)
        return self.email