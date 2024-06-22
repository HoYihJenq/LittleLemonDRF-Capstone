from django.test import TestCase
from .models import Menu
# Create your tests here.

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=5)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "IceCream : 80")

class Meowtest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Baklava", price=80, inventory=5)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "Baklavashhh : 80")
        