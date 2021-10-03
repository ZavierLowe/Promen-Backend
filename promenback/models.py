from django.db import models

# Create your models here.
class Customer(models.Model):
      username = models.CharField(max_length=150)
      first_name = models.CharField(max_length=150)
      email = models.CharField(max_length=150)
      password = models.CharField(max_length=150)
      
      def __str__(self):
            return self.username


class Product(models.Model):
      name = models.CharField(max_length=200)
      price = models.FloatField()
      description = models.CharField(max_length=500)
      photo_url = models.TextField()
      
      
      def __str__(self):
            return self.name
      


class FeaturedProduct(models.Model):
       name = models.CharField(max_length=200)
       price = models.FloatField()
       description = models.CharField(max_length=500)
       photo_url = models.TextField()
       
       def __str__(self):
            return self.name