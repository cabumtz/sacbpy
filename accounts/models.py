# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u"%s, %s" % (self.id, self.name)
        pass

    pass

class Account(models.Model):
    bank = models.ForeignKey(Bank)
    accountId = models.CharField(max_length=100)
    clabe = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return u"%s, %s, (%s)" % (self.id, self.accountId, self.bank)
        pass

    pass

class DebitCard(models.Model):
    EXPIRE_STATUS_ACTIVE='EA'
    EXPIRE_STATUS_EXPIRED='EE'

    STATUS_ACTIVE='A'
    STATUS_BLOCKED='B'
    STATUS_INACTIVE='I'
    STATUS_LOST='L'

    STATUS_CHOICES = (
            (STATUS_ACTIVE, 'Active'),
            (STATUS_BLOCKED, 'Blocked'),
            (STATUS_INACTIVE, 'Inactive'),
            (STATUS_LOST, 'Lost'),
        )

    EXPIRE_STATUS_CHOICES = (
            (EXPIRE_STATUS_ACTIVE, 'Active'),
            (EXPIRE_STATUS_EXPIRED, 'Expired'),
        )

    account = models.ForeignKey(Account)
    plasticId = models.CharField(max_length=100)
    expireDate = models.DateField()
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    expireStatus = models.CharField(max_length=5, choices=EXPIRE_STATUS_CHOICES, default=EXPIRE_STATUS_ACTIVE)

    def __unicode__(self):
        return u"(%s), %s, %s, %s" % (self.id, self.plasticId, self.status, self.expireStatus)
        pass

    pass

class Transaction(models.Model):
    code = models.CharField( max_length=50, blank=True, null=True)
    shortName = models.CharField( max_length=50, blank=True, null=True)
    description = models.CharField( max_length=200, blank=True, null=True)
    amount = models.FloatField()

    def __unicode__(self):
        return u"(%s), %s, %s, %s" % (self.id, self.code, self.shortName, self.amount)
        pass

    pass

class BalanceSnapshot(models.Model):
    debitCard = models.ForeignKey(DebitCard)
    #date = models.DateTimeField()
    strDate = models.CharField(max_length=50)
    strTime = models.CharField(max_length=50)
    transaction = models.ForeignKey(Transaction, null=True)
    amount = models.FloatField()

    def __unicode__(self):
        return u"(%s), %s, %s, %s" % (self.debitCard, self.strDate, self.strTime, self.amount)
        pass

    pass



