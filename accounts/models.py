from django.db import models

# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=200)
    pass

class Account(models.Model):
    bank = models.ForeignKey(Bank)
    accountId = models.CharField(max_length=100)
    clabe = models.CharField(max_length=100)
    pass

class DebitCard(models.Model):
    account = models.ForeignKey(Account)
    plasticId = models.CharField(max_length=100)
    expireDate = models.DateField()
    pass

class BalanceSnapshot(models.Model):
    account = models.ForeignKey(Account)
    date = models.DateTimeField()
    amount = models.FloatField()
    pass