from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from reviewer.revserviceimpl import ReviewerServiceImpl


@api_view(['POST'])
def register_reviewer(request):
    reviewer_data = request.data
    print(reviewer_data)
    ReviewerServiceImpl.register_reviewer(reviewer_data)
    return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def view_pending_review_items(request):
    pending_reviews = ReviewerServiceImpl.view_pending_reviews()
    print(pending_reviews)
    return Response({'pending_reviews': pending_reviews}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def approve_item(request):
    item_id = request.data
    print(item_id)
    ReviewerServiceImpl.approve_item(item_id)
    return Response(ReviewerServiceImpl.approve_item(item_id), status=status.HTTP_200_OK)

# Create your views here.
