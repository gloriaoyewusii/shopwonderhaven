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
    def validate_seller_details(seller_info):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$'
        if not re.match(pattern, seller_info.email):
            raise ValidationError('Invalid email')
        if seller_info.email is None or seller_info.email == '':
            raise Exception('Email cannot be empty')
        if seller_info.password is None or seller_info.password == '':
            raise Exception('Password cannot be empty')

    @staticmethod
    def submit_item(item_data):
        item_info = Item.objects.create(**item_data)
        ItemRepo.save_item_to_repo(item_info)
        return item_info

    @staticmethod
    def view_status(item_id):
        item = Item.objects.get(id=item_id)
        if item.status == 'pending':
            return 'Pending'
        elif item.status == 'approved':
            return 'Approved'
        else:
            return 'Rejected'