from django.contrib import admin
from .models import Product, Supplier, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Category)
