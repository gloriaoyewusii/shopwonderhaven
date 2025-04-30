from buyer.models import Buyer

from buyer.buyerrepointerface import BuyerRepoInterface

class BuyerRepo(BuyerRepoInterface):
    @staticmethod
    def save_buyer_to_repo(buyer):
        buyer.save()
        return buyer
    @staticmethod
    def count_buyers():
        return len(Buyer.objects.all())
    @staticmethod
    def find_buyer_by_id(buyer_id):
        buyer = Buyer.objects.get(id=buyer_id)
        return buyer
    @staticmethod
    def find_buyer_by_email(email):
        buyer = Buyer.objects.get(email=email)
        return buyer
    @staticmethod
    def delete_buyer_by_id(buyer_id):
        buyer = Buyer.objects.get(id=buyer_id)
        return buyer.delete()
    @staticmethod
    def find_all_buyers():
        return Buyer.objects.all()