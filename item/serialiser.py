from rest_framework import serializers
from item.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "title", "description", "starting_price", "quantity")