
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from buyer.buyerservice import BuyerService

@api_view(['POST'])
def register_buyer(request):
    buyer_data = request.data
    print(buyer_data)
    BuyerService.register(buyer_data)
    return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)

# Create your views here.
