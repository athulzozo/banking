import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(default=datetime.date(2024, 2, 27))
    number = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=6, choices=(('male', 'Male'), ('female', 'Female')))
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    district = models.CharField(max_length=50, choices=(('district1', 'District 1'), ('district2', 'District 2'), ('district3', 'District 3')))
    account = models.CharField(max_length=50, choices=(('Current Account', 'Current Account'), ('Savings', 'Savings'), ('Business Account', 'Business Account')))
    credit_card = models.BooleanField(default=False,blank=True)
    debit_card = models.BooleanField(default=False,blank=True)
    cheque_book = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.name
