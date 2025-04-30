from rest_framework import serializers
from buyer.models import Buyer

class BuyerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ("id", "first_name", "last_name", "email")