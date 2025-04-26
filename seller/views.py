from django.shortcuts import render

from seller.sellerservice import SellerService


def register_seller(seller_data):
    return SellerService.register(seller_data)

def submit_item(item_data):
    return SellerService.submit_item(item_data)

def view_review_status(item_id):
    return SellerService.view_review_status(item_id)
# class SellerViews(SellerService):
#
#     @staticmethod
#     def register_seller(seller_data):
#         return SellerService.register(seller_data)
#     @staticmethod
#     def submit_item(item_data):
#         return SellerService.submit_item(item_data)
#     @staticmethod
    # def view_review_status(item_id):
    #     return SellerService.view_review_status(item_id)
# Create your views here.
