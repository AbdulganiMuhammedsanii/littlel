from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu
#TestCase class
class MenuItemTest(TestCase):
   def test_get_item(self):
     item = Menu.objects.create(title="IceCream", price=80, inventory=100)
     self.assertEqual(item, "IceCream : 80")

def test_get_all(self):
      response = self.client.get(reverse('menuitem-list'))
      items = Menu.objects.all()
      serializer = MenuSerializer(items, many=True)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(response.data, serializer.data)