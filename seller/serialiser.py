from rest_framework import serializers
from seller.models import Seller

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ("id", "first_name", "last_name", "email")