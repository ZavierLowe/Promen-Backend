from django.contrib import admin
from .models import Customer
from .models import Product
from .models import FeaturedProduct

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(FeaturedProduct)