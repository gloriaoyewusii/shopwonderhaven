from django.db import models
class ReviewerServiceInterface(models.Model):
    class Meta:
        abstract = True

    @staticmethod
    def register_reviewer(reviewer):
        pass
    @staticmethod
    def approve_item(item_id):
        pass
    def reject_item(self):
        pass
    @staticmethod
    def view_pending_reviews():
        pass