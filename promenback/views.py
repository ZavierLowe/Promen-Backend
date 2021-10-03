from django.shortcuts import render
from .models import Product, Customer, FeaturedProduct
from rest_framework import generics
from .serializers import ProductSerializer, CustomerSerializer,FeaturedProductSerializer

# Create your views here.
class ProductList(generics.ListCreateAPIView):
      queryset = Product.objects.all()
      serializer_class = ProductSerializer
      
      
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerList(generics.ListCreateAPIView):
      queryset = Customer.objects.all()
      serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset = Customer.objects.all()
      serializer_class = CustomerSerializer 
      

class FeaturedProductList(generics.ListCreateAPIView):
      queryset = FeaturedProduct.objects.all()
      serializer_class = FeaturedProductSerializer

class FeaturedProductDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset = FeaturedProduct.objects.all()
      serializer_class = FeaturedProductSerializer