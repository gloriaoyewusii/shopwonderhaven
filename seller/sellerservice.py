
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
        try:
            seller_id = item_data["seller_id"]
            if not Seller.objects.get(id=seller_id):
            # if not Seller.objects.filter(id=seller_id).exists():
                raise ValidationError("Seller is not registered")
            else:
                item_info = Item.objects.create(**item_data)
                return item_info
        except Exception as e:
            raise ValidationError(e)



        # else:
        #     raise ValidationError("Seller is not registered")

            # if not Seller.objects.get(id=item.seller_id):
            #     raise ValidationError("Seller is not registered")
            # else:
            #     saved_item = ItemRepo.save_item_to_repo(**item_data)
            #     return saved_item


        # if Seller.objects.get(id=item_data.get(seller_id=)):
            # saved_item = Item.objects.create(**item_data)

            # else:



    @staticmethod
    def view_review_status(item_id):
        item = Item.objects.get(id=item_id)
        if item.status == 'pending':
            return {"Review Status: Pending"}
        elif item.status == 'approved':
            return {"Review Status": "Approved"}
        else:
            return '{"Review Status": "Rejected"}'
