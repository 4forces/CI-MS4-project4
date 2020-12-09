from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(blank=False, max_length=150)
    cost = models.FloatField(blank=False)
    # supplier = models.ForeignKey('Supplier', blank=True, null=True,
    #                              on_delete=models.CASCADE)
    unit = models.CharField(blank=False, max_length=10)
    quantity = models.IntegerField(blank=False, default=0)
    # category = models.ForeignKey('Category', blank=True, null=True,
    #                              on_delete=models.CASCADE)
    part_number = models.CharField(blank=False, max_length=15)
    desc = models.TextField(blank=False)

    def __str__(self):
        return self.name

