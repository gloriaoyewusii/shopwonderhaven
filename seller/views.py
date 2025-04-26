
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from seller.sellerservice import SellerService

@api_view(['POST'])
def register_seller(request):
    seller_data = request.data
    print(seller_data)
    SellerService.register(seller_data)
    return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)

    # return SellerService.register(seller_data)
@api_view(['POST'])
def submit_item(request):
    item_data = request.data
    print(item_data)
    SellerService.submit_item(item_data)
    return Response({'message': 'Item submitted'}, status=status.HTTP_200_OK)

def view_review_status(item_id):
    return SellerService.view_review_status(item_id)

# Create your views here.
