# Third-Party
from rest_framework import status
from rest_framework.test import APITestCase

# Django
from django.urls import reverse

# Local Django
from users.models import User


class TokenAPITestCase(APITestCase):

    def setUp(self):
        # Create User
        self.email = 'doit@unicrow.com'
        self.first_name = 'Doit'
        self.last_name = 'Apps'
        self.password = '123456test'
        self.user = User.objects.create_user(
            email=self.email, password=self.password
        )
        self.user.first_name = self.first_name
        self.user.last_name = self.last_name
        self.user.is_verified = True
        self.user.save()

    def test_login_verified(self):
        dummy_data = {
            'email': self.email,
            'password': self.password
        }
        url = reverse('login')

        response = self.client.post(url, dummy_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_unverified(self):
        dummy_data = {
            'email': self.email,
            'password': self.password
        }
        self.user.is_verified = False
        self.user.save()
        url = reverse('login')

        response = self.client.post(url, dummy_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ContactAPITestCase(APITestCase):
    dummy_data = {
        'first_name': 'Doit',
        'last_name': 'Apps',
        'email': 'doit@unicrow.com',
        'message': 'Good job!'
    }
