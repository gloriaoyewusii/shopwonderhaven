
from django.test import TestCase
from rest_framework.exceptions import ValidationError

import seller
from item.itemrepo import ItemRepo
from seller.sellerrepo import SellerRepo
from seller.sellerservice import SellerService
from seller.serialiser import SellerSerializer


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
    def test_that_seller_can_submit_item(self):
        seller_service = SellerService()
        seller1 = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jdoe@gmail.com",
            "password": "password"
        }
        seller_service.register(seller1)
#
        item = {
            "title":"Rare home jewels",
            "description":"A beauty, rare and remembered fondly for its starry allure.",
            "starting_price":"925,000"
        }
        seller_service.submit_item(item)
        self.assertEqual(ItemRepo.count_items(), 1)
#
#     def test_that_seller_cannot_register_with_empty_password(self):
#         seller_service = SellerService()
#         seller1 = {
#             "first_name": "John",
#             "last_name": "Doe",
#             "email": "jdoe@gmail.com",
#             "password": ""
#         }
#         self.assertEqual(seller_service.register(seller1), None)
#
#     def test_that_seller_cannot_register_with_wrong_email_format(self):
#         seller_service = SellerService()
#         seller1 = {
#             "first_name": "John",
#             "last_name": "Doe",
#             "email": "jdoegmail@.com",
#             "password": "password"
#         }
#         with self.assertRaises(ValidationError):
#             seller_service.register(seller1)
#
#             self.assertEqual(seller_service.register(seller1), None)
#
# # Create your tests here.
