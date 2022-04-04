""" Homepage tests """
from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User


class WelcomeViewTestCase(TestCase):
    """ setup information to run test """
    def setUp(self):
        self.username = "user"
        self.password = "valid_password1"
        self.client = Client()
        self.url = reverse("home")

        User.objects.create_user(
            self.username, "email@test.com", self.password)

    def test_home_sends_user_to_login(self):
        """ Test to run homepage and search for chosen text """
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ADVENTURE!")
