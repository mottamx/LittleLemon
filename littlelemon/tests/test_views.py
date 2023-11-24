from django.test import TestCase
from restaurant.views import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Dish1", price=10.99, inventory=2)
        Menu.objects.create(title="Dish2", price=15.99, inventory=3)

        self.client = APIClient()
        self.url = reverse('menu-list')

    def test_getall(self):
        response = self.client.get(self.url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_401_OK)
        self.assertEqual(response.data, serializer.data)