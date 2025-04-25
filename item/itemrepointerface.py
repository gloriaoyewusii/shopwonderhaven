from django.db import models


class ItemRepoInterface(models.Model):
    class Meta:
        abstract = True

    @staticmethod
    def save_item_to_repo(item):
        pass
    @staticmethod
    def count_items():
        pass
    @staticmethod
    def find_item_by_id(item_id):
        pass
    @staticmethod
    def delete_item_by_id(item_id):
        pass
    @staticmethod
    def find_all_items():
        pass
