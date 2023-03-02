from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('cart_add/<product_id>/', views.cart_add, name='cart_add'),
    path('cart_remove/<product_id>/', views.cart_remove,  name='cart_remove'),
]