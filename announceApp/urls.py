from django.urls import path,include
from . import views

app_name = 'announceApp'

urlpatterns = [
    path('',views.announce,name="announce"),
    path('announceDetail/<int:id>/', views.announceDetail, name="announceDetail" ),
]