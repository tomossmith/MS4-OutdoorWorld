""" Contact - tests.py """
from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .forms import ContactForm


class ViewTestCase(TestCase):
    """
    setup information to run test
    """
    def setUp(self):
        self.username = "user"
        self.password = "valid_password1"
        self.client = Client()
        self.url = reverse("contact")

        User.objects.create_user(
            self.username, "email@test.com", self.password)

    def test_contact_loads_correctly(self):
        """
        Test to run contact and search for chosen text
        """
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact")

    def test_empty_form(self):
        """
        Test to see if all fields load correctly
        """
        form = ContactForm()
        self.assertIn("name", form.fields)
        self.assertIn("email", form.fields)
        self.assertIn("subject", form.fields)
        self.assertIn("message", form.fields)
