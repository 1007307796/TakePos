from django.urls import path
from . import views

app_name = 'productApp'

urlpatterns = [
    path('products/<str:productName>/',views.products,name="products"),
    path('productDetail/<int:id>/',views.productDetail,name="productDetail"),
    path('createOrder/',views.createOrder,name="createOrder"),
    path('showData/',views.showData,name="showData")
]