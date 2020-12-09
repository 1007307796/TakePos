from django.test import TestCase
import unittest
from django.db.models import Count
from datetime import datetime
import os
from datetime import date
# Create your tests here.
from .models import User,UserOrder
from productApp.models import Product
class TestuserApp(unittest.TestCase):
 
    def setUp(self):
        print("do something befor test.prepare environment")
 
    def tearDown(self):
        print("do something after test.Clean up")

    # @unittest.skip("i don't want to run this case")
    def test_order(self):
        user = User.objects.get(username='superuser')
        orders = user.order_user.all()
        for order in orders:
            product = Product.objects.get(id=order.product_id)
            order.title = product.title
        for order in orders:
            print(order.__dict__)
            
    # class TestA(unittest.TestCase):
    #     print



if __name__ == '__main__':
    unittest.main()