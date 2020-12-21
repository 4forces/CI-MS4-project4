from django.urls import path
import cart.views

urlpatterns = [
    path('', cart.views.view_cart,
         name='view_cart'),
    path('add/<product_id>', cart.views.add_to_cart,
         name='add_to_cart'),
    path('minus/<product_id>', cart.views.minus_from_cart,
         name='minus_from_cart'),
    path('remove/<product_id>', cart.views.remove_from_cart,
         name='remove_from_cart'),
]
