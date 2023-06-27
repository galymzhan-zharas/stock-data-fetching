from tkinter import CASCADE
from django.db import models

# Create your models here.

class Company(models.Model):
    country = models.CharField()
    currency = models.CharField()
    estimateCurrency = models.CharField()
    exchange = models.CharField()
    ipo = models.DateTimeField()
    marketCapitalization = models.DecimalField(max_digits=30, decimal_places=20)
    name = models.CharField()
    phone = models.CharField()
    shareOutstanding = models.DecimalField(max_digits=30, decimal_places=20)
    ticker = models.CharField()
    weburl = models.CharField()
    logo = models.CharField()
    finnhubIndustry = models.CharField()

    def __str__(self):
        return self.name

class Stock(models.Model):
    company_profile = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    symbol = models.CharField()
    c = models.DecimalField(max_digits=10, decimal_places=4)
    d = models.DecimalField(max_digits=10, decimal_places=4)
    dp = models.DecimalField(max_digits=10, decimal_places=4)
    h = models.DecimalField(max_digits=10, decimal_places=4)
    l = models.DecimalField(max_digits=10, decimal_places=4)
    o = models.DecimalField(max_digits=10, decimal_places=4)
    pc = models.DecimalField(max_digits=10, decimal_places=4)
    t = models.BigIntegerField()
    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.symbol
