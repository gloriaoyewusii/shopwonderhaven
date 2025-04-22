from django.db import models

class ServiceInterface(models.Model):
    class Meta:
        abstract = True

    @staticmethod
    def register(seller_data):
       pass