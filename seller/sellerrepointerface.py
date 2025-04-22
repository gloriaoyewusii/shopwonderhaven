from django.db import models
class SellerRepoInterface(models.Model):
    class Meta:
        abstract = True
    @staticmethod
    def save_seller_to_repo(seller):
        pass
    @staticmethod
    def count_sellers():
        pass
    @staticmethod
    def find_seller_by_id(seller_id):
        pass
    @staticmethod
    def find_seller_by_email(email):
        pass
    @staticmethod
    def delete_seller_by_id(seller_id):
        pass
    @staticmethod
    def find_all_sellers():
        pass