from django.shortcuts import render, redirect, reverse, HttpResponse, \
    get_object_or_404
from django.contrib.auth.decorators import login_required

# import 'settings' and 'stripe' to access stripe key
from django.conf import settings
import stripe
import json

from products.models import Product
from .models import Purchase

from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


# Create your views here.


@login_required
def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # retrieve shopping cart
    cart = request.session.get('shopping_cart', {})

    # initiate empty lists
    line_items = []
    all_product_ids = []

    for product_id, product in cart.items():
        # retrieve product by its id from database
        product_model = get_object_or_404(Product, pk=product_id)

        # create line item
        # name, amount, currency and quantity: predefined by Stripe
        item = {
            "name": product_model.name,
            "amount": product_model.cost,
            "quantity": product['quantity'],
            "currency": "sgd",
        }

        line_items.append(item)
        all_product_ids.append({
            'product_id': product_model.id,
            'qty': product['quantity']
        })

    # assign current website to variable
    current_site = Site.objects.get_current()

    # assign site domain to variable
    domain = current_site.domain

    # create payment session for Stripe
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        client_reference_id=request.user.id,
        # metadata can only be str type
        metadata={
            'all_product_ids': json.dumps(all_product_ids)
        },
        mode="payment",
        success_url=domain + reverse('checkout_success'),
        cancel_url=domain + reverse('checkout_cancelled')
    )

    return render(request, "checkout/checkout.template.html", {
        'session_id': session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY
    })


def checkout_success(request):
    request.session['shopping_cart'] = {}
    return redirect(reverse("home"))


def checkout_cancelled(request):
    return redirect(reverse("view_cart"))


# From Stripe documentation
@csrf_exempt
def payment_completed(request):
    # Verifying data is sent by Stripe
    endpoint_secret = settings.ENDPOINT_SECRET
    payload = request.body
    # Retrieve Stripe Signature
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        print("Invalid payload")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Signature is invalid
        print("Invalid signature")
        return HttpResponse(status=400)

    # Processing the order
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        handle_payment(session)

    return HttpResponse(status=200)


def handle_payment(session):
    metadata = session['metadata']
    user = get_object_or_404(User, pk=session['client_reference_id'])
    # covert json 'metadata' to python list nested dictionary object
    all_product_ids = json.loads(metadata['all_product_ids'])

    for order_item in all_product_ids:
        product_model = get_object_or_404(Product, pk=order_item['product_id'])

        # create 'purchase' model manually
        purchase = Purchase()
        purchase.product_id = product_model
        purchase.user_id = user
        purchase.qty = order_item['qty']
        purchase.price = product_model.cost

        # save the created purchase model
        purchase.save()
