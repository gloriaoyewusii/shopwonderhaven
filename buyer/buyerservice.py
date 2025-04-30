from rest_framework.exceptions import ValidationError


from buyer.models import Buyer
from buyer.buyerrepo import BuyerRepo
from buyer.serialiser import BuyerSerialiser
from buyer.buyerserviceinterface import BuyerInterface

class BuyerService(BuyerInterface):

    @staticmethod
    def register(buyer_data):
        buyer_serialiser = BuyerSerialiser(data=buyer_data)

        if buyer_serialiser.is_valid():
            saved_buyer = buyer_serialiser.save()
            return saved_buyer
        else:
            raise ValidationError(buyer_serialiser.errors)