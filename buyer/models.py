
from django.db import models


class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    password = models.CharField(max_length=50, null=False, blank=False)


# Create your models here.
