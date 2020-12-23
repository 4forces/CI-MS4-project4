from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Product(models.Model):
    name = models.CharField(blank=False, max_length=150)
    cost = models.DecimalField(blank=False, max_digits=10, decimal_places=3)
    unit = models.CharField(blank=False, max_length=10)
    quantity = models.IntegerField(blank=False, default=0)
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE, default=1)
    part_number = models.CharField(blank=False, max_length=15)
    description = models.TextField(blank=False)
    buyer = models.ForeignKey(User,
                              on_delete=models.CASCADE, default=1)
    supplier = models.ForeignKey('Supplier',
                                 on_delete=models.CASCADE, default=1)
    cover = CloudinaryField()

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(blank=False, max_length=30)
    country = models.CharField(blank=True, max_length=90)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(blank=False, max_length=30)

    def __str__(self):
        return self.name
