
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.utils import json

from seller.sellerservice import SellerService

@api_view(['POST'])
def register_seller(request):
    seller_data = request.data
    print(seller_data)
    # v_data = json.load(seller_data)
    # print(v_data)
    SellerService.register(seller_data)
    return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)

    # return SellerService.register(seller_data)

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
