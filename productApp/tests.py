# -*- coding: utf-8 -*-
 
import unittest
from productApp.models import Product 
from django.db.models import Count
from datetime import datetime
import os
from datetime import date
 
class TestproductApp(unittest.TestCase):
 
    def setUp(self):
        print("do something befor test.prepare environment")
 
    def tearDown(self):
        print("do something after test.Clean up")

    # @unittest.skip("i don't want to run this case")
    def test_time(self):
        labels = []
        class Labels(object):

            def __init__(self,pid,pname,pcount):
                self.pid = pid
                self.pname = pname
                self.pcount = pcount

        productList = Product.objects.all()
        label = Labels(pid="all",pname="所有类型",pcount=len(productList))
        labels.append(label)
        label_ed = Labels(pid="education",pname="学历类考试",pcount=0)
        label_te = Labels(pid="technology",pname="计算机类考试",pcount=0)
        label_ec = Labels(pid="economic",pname="金融类考试",pcount=0)
        label_la = Labels(pid="language",pname="语言类考试",pcount=0)
        for product in productList:
            if product.productType == label_ed.pid:
                label_ed.pcount += 1
            if product.productType == label_te.pid:
                label_te.pcount += 1
            if product.productType == label_ec.pid:
                label_ec.pcount += 1
            if product.productType == label_la.pid:
                label_la.pcount += 1
        labels.extend([label_ed,label_te,label_ec,label_la])

    class TestA(unittest.TestCase):
        print



if __name__ == '__main__':
    unittest.main()
