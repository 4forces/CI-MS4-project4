from django.urls import path, include
import products.views

urlpatterns = [
    path('', products.views.index,
         name='view_all_products'),
]
