from rest_framework import serializers
from .models import Product, Customer, FeaturedProduct


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
          model = Product
          fields = ('id','name','price','description','photo_url')



class CustomerSerializer(serializers.HyperlinkedModelSerializer):
        
        class Meta:
            model = Customer
            fields = ('id','username','password','email','first_name')
            


class FeaturedProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeaturedProduct
        fields =('id','name','price','description','photo_url')