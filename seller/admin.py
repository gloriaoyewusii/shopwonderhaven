from django.contrib import admin

from item.models import Item
from seller.models import Seller
from buyer.models import Buyer

admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Item)
# Register your models here.
