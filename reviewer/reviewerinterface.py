from django.db import models


class ReviewerInterface(models.Model):
    class Meta:
        abstract = True

    @staticmethod
    def save_reviewer_to_repo(reviewer):
        pass
    @staticmethod
    def count_reviewer():
        pass
    @staticmethod
    def find_reviewer_by_id(reviewer_id):
        pass
    @staticmethod
    def delete_reviewer_by_id(reviewer_id):
        pass
    @staticmethod
    def find_all_reviewers():
        pass
