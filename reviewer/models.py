from django.db import models
class Reviewer(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, unique=True, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
# Create your models here.
