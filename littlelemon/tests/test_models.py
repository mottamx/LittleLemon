from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Tacos pastor', price=50, inventory=6)
        itemstr = str(item)
        
        self.assertEqual(itemstr, "Tacos pastor : 50")