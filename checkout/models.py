from django.db import models

from products.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Purchase(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=False)
    qty = models.IntegerField(blank=False)

    def __str__(self):
        title = (
            f"Purchase for product "
            f"#{self.product_id.id} by user#{self.user_id.id}"
        )
        return title
