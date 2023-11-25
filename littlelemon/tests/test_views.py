from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token

from restaurant.views import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(APITestCase):
    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer 0c56e6181c72efc15602be1706efa5c4ef4d0579')
        Menu.objects.create(title="Dish2", price=10.99, inventory=2)
        self.url = reverse('menu-list')

    def test_getall_authenticated(self):
        response = self.client.get(self.url)
        #print(response.content)  # Print the response content
        last_menu = Menu.objects.last()
        serializer = MenuSerializer([last_menu], many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)