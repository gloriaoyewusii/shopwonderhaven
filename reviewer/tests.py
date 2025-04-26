from django.test import TestCase
from rest_framework.exceptions import ValidationError

from item.itemrepo import ItemRepo
from reviewer.reviewersrepo import ReviewersRepo
from reviewer.revserviceimpl import ReviewerServiceImpl
from seller.sellerrepo import SellerRepo
from seller.sellerservice import SellerService


class TestReviewerService(TestCase):
    def test_that_reviewer_cannot_register_with_incomplete_details(self):
        reviewer_service = ReviewerServiceImpl()
        reviewer1 = {
            "first_name": " ",
            "last_name": "Doe",
            "email": "jdoe gmail.com",
            "password": " "
        }

        with self.assertRaises(ValidationError):
            reviewer_service.register_reviewer(reviewer1)
        # self.assertEqual(registered_reviewer.first_name, "John")
        rev_repo = ReviewersRepo()
        self.assertEqual(rev_repo.count_reviewer(), 0)

    def test_that_reviewer_can_register_with_correct_details(self):
        reviewer_service = ReviewerServiceImpl()
        reviewer1 = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "jdoe@gmail.com",
            "password": "hashedPassword"
        }
        registered_reviewer = reviewer_service.register_reviewer(reviewer1)
        self.assertEqual(registered_reviewer.first_name, "John")
        self.assertEqual(registered_reviewer.last_name, "Doe")
        self.assertEqual(registered_reviewer.email, "jdoe@gmail.com")
        rev_repo = ReviewersRepo()
        self.assertEqual(rev_repo.count_reviewer(), 1)

    def test_that_registered_seller_submits_item_reviewer_views_pending_reviews_when_reviewer_approves_item_returns_approved(self):
        reviewer_service = ReviewerServiceImpl()
        seller_service = SellerService()
        seller1 = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "jdoe@gmail.com",
            "password": "hashedPassword"
        }
        registered_seller = seller_service.register(seller1)
        self.assertEqual(registered_seller.first_name, "John")

        seller_repo = SellerRepo()
        self.assertEqual(seller_repo.count_sellers(), 1)

        reviewer = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jaydoe@gmail.com",
            "password": "strongword"
        }
        registered_reviewer = reviewer_service.register_reviewer(reviewer)
        self.assertEqual(registered_reviewer.first_name, "Jane")

        rev_repo = ReviewersRepo()
        self.assertEqual(rev_repo.count_reviewer(), 1)

        item = {
            "seller_id": registered_seller.id,
            "title":"Paolo Venini Italian Mid-Century Glass Scroll Chandelier",
            "description":"""Italian Mid-Century (1940s) clear glass chandelier with 6 upright scrolls & 6 scroll
             form arms holding large round bowl form shades with glass drops and emanating from a tiered center shaft. (PAOLO VENINI).
             """,
            "starting_price": 18500.00,
            "quantity": 1
        }
        submitted_item = seller_service.submit_item(item)
        item_repo = ItemRepo()

        self.assertEqual(item_repo.count_items(), 1)

        pending_items = reviewer_service.view_pending_reviews()
        self.assertEqual(len(pending_items), 1)
        for index in range(len(pending_items)):
            self.assertEqual(pending_items[index].title, item["title"])

        self.assertEqual(reviewer_service.approve_item(1), {"Review Status": "Approved"})

        self.assertEqual(seller_service.view_review_status(submitted_item.id), {"Review Status": "Approved"})


# Create your tests here.
