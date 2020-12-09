from django.shortcuts import render
from .models import SucceededUser
from productApp.models import Product 
from userApp.models import User
from time import sleep
from datetime import datetime
from django.views.decorators.cache import cache_page
# @cache_page(60*15)

# Create your views here.
def home(request):
    users = SucceededUser.objects.all().order_by('-timeend')[:20]
    for user in users:
        t = user.timeend-user.timestart
        secs = t.seconds
        days = str(t.days) + '天' if t.days else ''
        hours = str(secs//3600) + '时' if secs//3600 else ''
        minutes = str(secs%3600//60) + '分' if secs%3600//60 else ''
        seconds = str(secs%3600%60) + '秒' if secs%3600%60 else ''
        user.cost = ''.join(map(lambda x:x.strip(),(days,hours,minutes,seconds)))
    
    productList = Product.objects.all().order_by('-views')
    productList = productList[0:4]

    return render(request,'home.html',{
        'active_menu' : 'home',
        'users' : users,
        'productList': productList,
    })