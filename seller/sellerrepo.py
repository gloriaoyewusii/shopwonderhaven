from seller.models import Seller
from seller.sellerrepointerface import SellerRepoInterface

class SellerRepo(SellerRepoInterface):
    @staticmethod
    def save_seller_to_repo(seller):
        seller.save()
        return seller
    @staticmethod
    def count_sellers():
        return len(Seller.objects.all())
    @staticmethod
    def find_seller_by_id(seller_id):
        seller = Seller.objects.get(id=seller_id)
        return seller
    @staticmethod
    def find_seller_by_email(email):
        seller = Seller.objects.get(email=email)
        return seller
    @staticmethod
    def delete_seller_by_id(seller_id):
        seller = Seller.objects.get(id=seller_id)
        return seller.delete()
    @staticmethod
    def find_all_sellers():
        return Seller.objects.all()