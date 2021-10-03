from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
     
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('products/<str:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('customers/', views.CustomerList.as_view(), name='customer_list'),
    path('customers/<int:pk>',views.CustomerDetail.as_view(), name='customer_detail'),
    path('featuredproducts/', views.FeaturedProductList.as_view(), name='featuredproduct_list'),
    path('featuredproducts/<int:pk>',views.FeaturedProductDetail.as_view(), name='featuredproduct_detail'),
    
]