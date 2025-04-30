from django.db import models
from rest_framework import validators

from item.status import Status
from seller.models import Seller


class Item(models.Model):
    # id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=False)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    status = models.CharField(max_length=8, default=Status.PENDING, null=False, blank=False)

# Create your models here.
