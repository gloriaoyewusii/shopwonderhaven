from rest_framework.exceptions import ValidationError

from item.models import Item
from item.serialiser import ItemSerializer
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

        item_serializer = ItemSerializer(pending_reviews, many=True)
        return item_serializer.data


    @staticmethod
    def approve_item(item_id):
        item = Item.objects.get(id=item_id)
        if item.status == Status.PENDING and item.status != Status.REJECTED:
            item.status = Status.APPROVED
            item.save()
            return {item.title: "Approved"}
        elif item.status == Status.APPROVED:
            return {item.title: "Approved"}

    @staticmethod
    def reject_item(item_id):
        item = Item.objects.get(id=item_id)
        if item.status == Status.PENDING and item.status != Status.APPROVED:
            item.status = Status.REJECTED
            item.save()
            return {item.title: "Rejected"}
        elif item.status == Status.REJECTED:
            return {item.title: "Rejected"}
