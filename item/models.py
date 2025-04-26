from django.db import models

from item.status import Status


class Item(models.Model):
    # id = models.AutoField(primary_key=True)
    seller_id = models.IntegerField(null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    quantity = models.IntegerField(default=1, null=False, blank=False)
    status = models.CharField(max_length=8, default=Status.PENDING, null=False, blank=False)

# Create your models here.
