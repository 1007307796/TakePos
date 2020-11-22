# -*- coding: utf-8 -*-
 
import unittest
from homeApp.models import SucceededUser
from productApp.models import Product
from datetime import datetime
import os
from datetime import date
 
class TesthomeApp(unittest.TestCase):
 
    def setUp(self):
        print("do something befor test.prepare environment")
 
    def tearDown(self):
        print("do something after test.Clean up")

    @unittest.skip("i don't want to run this case")
    def test_time(self):
        users = SucceededUser.objects.all()
        for user in users:
            t = user.timeend-user.timestart
            secs = t.seconds
            days = str(t.days) + '天' if t.days else ''
            hours = str(secs//3600) + '时' if secs//3600 else ''
            minutes = str(secs%3600//60) + '分' if secs%3600//60 else ''
            seconds = str(secs%3600%60) + '秒' if secs%3600%60 else ''
            print(''.join(map(lambda x:x.strip(),(days,hours,minutes,seconds))))
    
    def test_slice(self):
        # Products = Product.objects.all().order_by('-views')
        # Products = Products[0:1]
        # print(Products)
        p = [1,2,3,4,5]
        p = p[0:4]
        print(p)
if __name__ == '__main__':
    unittest.main()
