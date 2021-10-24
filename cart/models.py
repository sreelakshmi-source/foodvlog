from django.db import models
from home.models import *


# Create your models here.

class cart(models.Model):
	cart_id=models.CharField(max_length=250,unique=True)
	date=models.DateTimeField(auto_now_add=True)
class cartitem(models.Model):
    prod_seltd = models.ForeignKey(prdct, on_delete=models.CASCADE)
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    qty=models.IntegerField()
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.prod_seltd
    def total(self):
        return self.qty*self.prod_seltd.price