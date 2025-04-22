from seller.models import Seller
from seller.sellerrepo import SellerRepo
from seller.serviceinterface import ServiceInterface

class SellerService(ServiceInterface):

    @staticmethod
    def register(seller_data):
        seller_info = Seller.objects.create(**seller_data)
        SellerRepo.save_seller_to_repo(seller_info)
        return seller_info