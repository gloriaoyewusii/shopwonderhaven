from rest_framework import serializers
from reviewer.models import Reviewer

class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = ('id', 'first_name', 'last_name', 'email')
