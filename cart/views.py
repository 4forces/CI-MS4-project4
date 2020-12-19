from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from products.models import Product

# Create your views here.


def add_to_cart(request, product_id):
    # get existing cart from session storage
    # key = 'shopping_cart'
    cart = request.session.get('shopping_cart', {})

    if product_id not in cart:
        product = get_object_or_404(Product, pk=product_id)
        # add to cart
        cart[product_id] = {
            'id': product_id,
            'item': Product.name,
            'quantity': 1,
            'price': float(Product.cost),
            'sub_total': float(Product.cost),
        }

        # save cart to sessions
        request.session['shopping_cart'] = cart

        message.success(request, "Item added to cart.")
        return redirect('view_shop')
    else:
        cart[product_id]['quantity'] += 1

    request.session['shopping_cart'] = cart
    return redirect('view_shop')