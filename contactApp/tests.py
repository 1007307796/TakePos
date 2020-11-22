# -*- coding: utf-8 -*-
 
import unittest
from contactApp.models import SchoolToPoint 
from datetime import datetime
import os
from datetime import date
 
class TestcontactApp(unittest.TestCase):
 
    def setUp(self):
        print("do something befor test.prepare environment")
 
    def tearDown(self):
        print("do something after test.Clean up")

    @unittest.skip("i don't want to run this case")
    def test_buyermap(self):
        points = SchoolToPoint.objects.all()
        datalist = []
        for item in points:
            data = {}
            data['name'] = item.name
            data['latitude'] = float(item.latitude)
            data['longitude'] = float(item.longitude)
            datalist.append(data)
        print(datalist)

    def test_message(self):
        print(date.time())
 
 
if __name__ == '__main__':
    unittest.main()
