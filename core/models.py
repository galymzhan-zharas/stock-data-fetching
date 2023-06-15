from django.db import models

# Create your models here.

class Stock(models.Model):
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
