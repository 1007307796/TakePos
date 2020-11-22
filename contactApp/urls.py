from django.urls import path
from . import views

app_name = 'contactApp'

urlpatterns = [
    path('help/',views.help,name="help"),
    path('message/',views.message,name="message"),
    path('more/',views.more,name="more"),
    path('download/',views.download,name="download"),
    path('platform/', views.platform, name='platform'),
    path('getFile/<int:id>/', views.getFile,name="getFile"),
    path('facedetect/',views.facedetect,name="facedetect"),
    path('buyermap/',views.buyermap,name="buyermap"),
]