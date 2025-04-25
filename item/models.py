from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    starting_price = models.CharField(max_length=7, null=False, blank=False)

# Create your models here.
