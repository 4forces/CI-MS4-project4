from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages

from products.models import Product

# Create your views here.


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # get existing cart from session storage
    # key = 'shopping_cart'
    cart = request.session.get('shopping_cart', {})

    if product_id not in cart:
        product = get_object_or_404(Product, pk=product_id)
        # if product is found, add it to cart
        cart[product_id] = {
            'id': product_id,
            'name': product.name,
            'quantity': 1,
            'cost': product.cost,
            'sub_total': product.cost,
            'cover': str(product.cover)
        }

        # request.session['shopping_cart'] = cart
        # return redirect('view_shop')
    else:
        # add qty +1 of product
        cart[product_id]['quantity'] += 1

    # save cart to sessions
    request.session['shopping_cart'] = cart
    print(cart)
    messages.success(request, "Item added to cart.")
    return redirect(reverse('view_shop'))


def view_cart(request):
    # get existing cart from session storage
    # key = 'shopping_cart'
    cart = request.session.get('shopping_cart', {})
    print(cart)
    return render(request, 'cart/cart_view.template.html', {
        'shopping_cart': cart
    })


def remove_from_cart(request, product_id):
    cart = request.session.get('shopping_cart', {})

    if product_id in cart:
        # remove it from the cart
        del cart[product_id]
        # save back to the session
        request.session['shopping_cart'] = cart
        messages.warning(request, "Item removed from cart")

    return redirect(reverse('view_cart'))
