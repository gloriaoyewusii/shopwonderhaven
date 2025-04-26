from django.db import models

class ServiceInterface(models.Model):
    class Meta:
        abstract = True

    @staticmethod
    def register(seller_data):
       pass
    @staticmethod
    def submit_item(item_data):
        pass
    @staticmethod
    def view_review_status(item_id):
        pass
