from django.db import models

class BuyerInterface(models.Model):
    class Meta:
        abstract = True

    @staticmethod
    def register(buyer_data):
       pass

    @staticmethod
    def view_all_items():
        pass
