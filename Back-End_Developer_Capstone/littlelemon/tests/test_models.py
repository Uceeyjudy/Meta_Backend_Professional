from django.test import TestCase
from django.urls import reverse
import json

from restaurant.serializers import MenuSerializer, BookingSerializer
from restaurant.models import Menu, Booking

# Create your tests here.
#TestCase classs
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item = str(item)
        self.assertEqual(item, "IceCream : 80")