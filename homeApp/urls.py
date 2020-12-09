from django.urls import path
from . import views

app_name = 'hometApp'

urlpatterns = [
    path('',views.home,name="home"),
]