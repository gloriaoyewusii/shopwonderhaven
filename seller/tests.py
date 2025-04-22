from django.test import TestCase

import seller
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
        seller_service.register(seller1)
        self.assertEqual(seller1.get("first_name"), "John")
        self.assertEqual(SellerRepo.count_sellers(), 1)
        seller2 = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane@gmail.com",
            "password": "password"
        }
        seller_service.register(seller2)
        self.assertEqual(SellerRepo.count_sellers(), 2)

    def test_that_if_seller_is_registered_seller_cannot_register_twice(self):
        seller_service = SellerService()
        seller1 = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "jdoe@gmail.com",
            "password": "password"
        }
        seller_service.register(seller1)
        seller2 = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jdoe@gmail.com",
            "password": "password"
        }

# Create your tests here.
