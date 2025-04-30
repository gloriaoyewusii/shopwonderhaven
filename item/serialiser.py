from rest_framework import serializers
from item.models import Item
from seller.models import Seller


class ItemSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())

    class Meta:
        model = Item
        fields = ("seller", "title", "description", "starting_price")