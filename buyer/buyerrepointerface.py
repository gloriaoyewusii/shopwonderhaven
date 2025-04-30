from django.db import models
class BuyerRepoInterface(models.Model):
    class Meta:
        abstract = True
    @staticmethod
    def save_buyer_to_repo(seller):
        pass
    @staticmethod
    def count_buyers():
        pass
    @staticmethod
    def find_buyer_by_id(seller_id):
        pass
    @staticmethod
    def find_buyer_by_email(email):
        pass
    @staticmethod
    def delete_buyer_by_id(seller_id):
        pass
    @staticmethod
    def find_all_buyers():
        pass