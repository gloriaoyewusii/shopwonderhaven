import re

from rest_framework.exceptions import ValidationError

from item.itemrepo import ItemRepo
from item.models import Item
from seller.models import Seller
from seller.sellerrepo import SellerRepo
from seller.serialiser import SellerSerializer
from seller.serviceinterface import ServiceInterface

class SellerService(ServiceInterface):

    @staticmethod
    def register(seller_data):
        seller_serialiser = SellerSerializer(data=seller_data)

        if seller_serialiser.is_valid():
            saved_seller = seller_serialiser.save()
            return saved_seller
        else:
            raise ValidationError(seller_serialiser.errors)

    @staticmethod
    def submit_item(item_data):
        # item_info = Item.objects.create(**item_data)
        # sellers_id = item_info.seller_id
        if Seller.objects.filter(id=item_data["seller_id"]).exists():
            # saved_item = Item.objects.create(**item_data)
            saved_item =  ItemRepo.save_item_to_repo(**item_data)
            return saved_item
        else:
            raise ValidationError("Seller is not registered")


    @staticmethod
    def view_review_status(item_id):
        item = Item.objects.get(id=item_id)
        if item.status == 'pending':
            return 'Pending'
        elif item.status == 'approved':
            return 'Approved'
        else:
            return 'Rejected'