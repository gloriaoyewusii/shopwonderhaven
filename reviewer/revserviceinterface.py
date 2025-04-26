from django.db import models
class ReviewerServiceInterface(models.Model):
    class Meta:
        abstract = True

    @staticmethod
    def register_reviewer(reviewer):
        pass
    def approve_item(self):
        pass
    def reject_item(self):
        pass
    @staticmethod
    def view_pending_reviews():
        pass