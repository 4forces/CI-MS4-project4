from django.urls import path, include
import products.views

urlpatterns = [
    path('shop', products.views.view_shop,
         name='view_shop'),
    path('view/<product_id>', products.views.view_single_product,
         name='view_single_product'),
    path('create', products.views.create_product),
    path('create-category', products.views.create_category),
    path('create-supplier', products.views.create_supplier),
]
