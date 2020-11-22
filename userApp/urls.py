from django.urls import path
from . import views

app_name = 'userApp'

urlpatterns = [
    path('register/',views.register,name="register"),
    path('userhome/',views.userhome,name="userhome"),
]