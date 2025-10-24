from decimal import Decimal

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuItemTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(username="testuser", password="testpass")
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

        Menu.objects.create(title="Pizza", price=Decimal("12.50"), inventory=10)
        Menu.objects.create(title="Pasta", price=Decimal("9.99"), inventory=5)
        Menu.objects.create(title="Salad", price=Decimal("6.00"), inventory=20)

    def test_get_menu_items(self):
        url = reverse("menu_items")
        print(url, "====================")
        print(type(url))

        response = self.client.get(url)
        print(response.status_code, "====================", response)
        print(type(response))

        serialized = MenuSerializer(Menu.objects.all(), many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serialized.data)
