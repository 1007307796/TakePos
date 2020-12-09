from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'userApp'

urlpatterns = [
    path('',views.register,name="register"),
    path('register/',views.register,name="register"),
    path('userhome/',views.userhome,name="userhome"),
]