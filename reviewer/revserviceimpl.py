from rest_framework.exceptions import ValidationError

from item.models import Item
from item.status import Status
from reviewer.revserviceinterface import ReviewerServiceInterface
from reviewer.serialiser import ReviewerSerializer


class ReviewerServiceImpl(ReviewerServiceInterface):

    @staticmethod
    def register_reviewer(reviewer_data):
        reviewer_serialiser = ReviewerSerializer(data=reviewer_data)

        if reviewer_serialiser.is_valid():
            saved_reviewer = reviewer_serialiser.save()
            return saved_reviewer
        else:
            raise ValidationError(reviewer_serialiser.errors)

    @staticmethod
    def view_pending_reviews():
        pending_reviews = []
        items = Item.objects.all()
        for item in items:
            if item.status == Status.PENDING:
                pending_reviews.append(item)
        return pending_reviews




