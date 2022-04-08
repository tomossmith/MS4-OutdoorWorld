""" Products - tests.py """
from django.test import TestCase, Client
from django.contrib.auth.models import User


class ViewTestCase(TestCase):
    """
    setup information to run test
    """
    def setUp(self):
        self.username = "user"
        self.password = "valid_password1"
        self.client = Client()
        self.url = '/products/'

        User.objects.create_user(
            self.username, "email@test.com", self.password)

    def test_products_load_correctly(self):
        """
        Test to run products and search for chosen text
        """
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Products")
