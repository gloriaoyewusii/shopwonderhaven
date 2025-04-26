from reviewer.models import Reviewer
from reviewer.reviewerinterface import ReviewerInterface


class ReviewersRepo(ReviewerInterface):

    @staticmethod
    def save_reviewer_to_repo(reviewer):
        reviewer.save()
        return reviewer
    @staticmethod
    def count_reviewer():
        count = Reviewer.objects.count()
        return count
    @staticmethod
    def find_reviewer_by_id(reviewer_id):
        reviewer = Reviewer.objects.get(id=reviewer_id)
        return reviewer
    @staticmethod
    def delete_reviewer_by_id(reviewer_id):
        reviewer = Reviewer.objects.get(id=reviewer_id)
        return reviewer.delete()
    @staticmethod
    def find_all_reviewers():
        return Reviewer.objects.all()
