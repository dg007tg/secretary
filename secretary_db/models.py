from django.db import models

# Create your models here.

class User(models.Model):
    account=models.CharField(max_length=16)
    password=models.CharField(max_length=16)
    authority=models.IntegerField(0)
class Salary(models.Model):
    name=models.CharField(max_length=32)
    amount=models.FloatField(0)
    date=models.DateTimeField(auto_now=False,auto_now_add=False)
    title=models.CharField(max_length=32)
class Bankinfo(models.Model):
    name=models.CharField(max_length=20)
    account=models.IntegerField(0)
    bank=models.TextField()
    balance=models.IntegerField(0)
    fund_change=models.IntegerField(0)
class Fee(models.Model):
    types=models.CharField(max_length=32)
    name=models.CharField(max_length=32)
    amount=models.FloatField(0)
    date=models.DateTimeField(auto_now=False,auto_now_add=False)
