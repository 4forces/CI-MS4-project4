from django.urls import path, include
import products.views

urlpatterns = [
    path('shop', products.views.view_shop,
         name='view_shop'),
    path('view/<product_id>', products.views.view_single_product,
         name='view_single_product'),
]
