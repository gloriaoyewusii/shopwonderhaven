
from django.test import TestCase
from rest_framework.exceptions import ValidationError

from item.itemrepo import ItemRepo
from seller.sellerrepo import SellerRepo
from seller.sellerservice import SellerService



class TestSellerService(TestCase):
    def test_that_seller_can_register(self):
        seller_service = SellerService()
        seller1 = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "jdoe@gmail.com",
            "password": "password"
        }

        seller2 = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "doej@gmail.com",
            "password": "password"
        }
        seller_service.register(seller1)
        seller_service.register(seller2)
        self.assertEqual(seller1.get("first_name"), "John")
        self.assertEqual(SellerRepo.count_sellers(), 2)

class TestSellerSerialiser(TestCase):
    def test_that_seller_data_is_valid(self):
        seller1 = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "jdoe@gmail.com",
            "password": "password"
        }
        # serialiser = SellerSerializer(data=seller1)
        # self.assertTrue(serialiser.is_valid())
        # validated_seller = serialiser.validated_data

        seller_service = SellerService()
        registered_seller = seller_service.register(seller1)
        self.assertEqual(registered_seller.first_name, "John")

        self.assertEqual(SellerRepo.count_sellers(), 1)

    def test_that_seller_data_is_invalid(self):
        seller2 = {
            "first_name": "",
            "last_name": "Doe",
            "email": "jdoe gmail. @ com",
            "password": "password"
        }

        # serialiser = SellerSerializer(data=seller2)
        # self.assertFalse(serialiser.is_valid())
        # self.assertIn("first_name", serialiser.errors)
        # self.assertIn("email", serialiser.errors)
        seller_service = SellerService()
        with self.assertRaises(ValidationError):
            seller_service.register(seller2)
    def test_that_if_seller_is_registered_seller_cannot_register_twice_with_same_email(self):
        seller_service = SellerService()
        seller1 = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "jdoe@gmail.com",
            "password": "password"
        }
        registered_seller = seller_service.register(seller1)
        seller2 = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jdoe@gmail.com",
            "password": "password"
        }
        with self.assertRaises(ValidationError):
            seller_service.register(seller2)

        self.assertEqual(registered_seller.first_name, "John")
        self.assertEqual(SellerRepo.count_sellers(), 1)
        self.assertEqual(registered_seller.id, 1)
#
    def test_that_seller_can_submit_item_for_review(self):
        seller_service = SellerService()
        seller_1 = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jdoe@gmail.com",
            "password": "password"
        }
        registered_seller = seller_service.register(seller_1)
#
        item = {
            "seller_id":registered_seller.id,
            "title":"Rare home jewels",
            "description":"A beauty, rare and remembered fondly for its starry allure.",
            "starting_price":925000.00,
            "quantity":1
        }
        seller_service.submit_item(item)
        self.assertEqual(ItemRepo.count_items(), 1)

    def test_that_item_is_submitted_when_seller_checks_review_status_returns_pending(self):
        seller_service = SellerService
        seller1 = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jdoe@gmail.com",
            "password": "password"
        }
        registered_seller = seller_service.register(seller1)
        #
        item = {
            "seller_id":registered_seller.id,
            "title": "Rare home jewels",
            "description": "A beauty, rare and remembered fondly for its starry allure.",
            "starting_price": 925000.00,
            "quantity": 1
        }
        seller_service.submit_item(item)

        item2 = {
            "seller_id":registered_seller.id,
            "title": "Pride and Prejudice, first edition",
            "description": "1867 copy of first edition of Jane Austen",
            "starting_price": 5000000.00,
            "quantity": 2
        }
        seller_service.submit_item(item2)
        self.assertEqual({"Review Status: Pending"}, seller_service.view_review_status(1))
        self.assertEqual({"Review Status: Pending"}, seller_service.view_review_status(2))


    def test_that_item_cannot_be_submitted_by_non_registered_seller(self):
        item = {
            "seller_id": 1,
            "title": "Paolo Venini Italian Mid-Century Glass Scroll Chandelier",
            "description": """Italian Mid-Century (1940s) clear glass chandelier with 6 upright scrolls & 6 scroll
                   form arms holding large round bowl form shades with glass drops and emanating from a tiered center shaft. (PAOLO VENINI).
                   """,
            "starting_price": 18500.00,
            "quantity": 1
        }
        item_repo = ItemRepo()
        seller_service = SellerService()
        with self.assertRaises(ValidationError):
            seller_service.submit_item(item)
        self.assertEqual(item_repo.count_items(), 0)


