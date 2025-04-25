from item.itemrepointerface import ItemRepoInterface
from item.models import Item


class ItemRepo(ItemRepoInterface):

    @staticmethod
    def save_item_to_repo(item):
        item.save()
        return item
    @staticmethod
    def count_items():
        return len(Item.objects.all())
    @staticmethod
    def find_item_by_id(item_id):
        item = Item.objects.get(id=item_id)
        return item
    @staticmethod
    def delete_item_by_id(item_id):
        item = Item.objects.get(id=item_id)
        return item.delete()
    @staticmethod
    def find_all_items():
        return Item.objects.all()