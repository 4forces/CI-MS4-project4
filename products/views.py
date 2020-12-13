from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import SearchForm


# Create your views here.
def view_shop(request):
    # return HttpResponse("Welcome to Products App")
    products = Product.objects.all()
    search_form = SearchForm(request.GET)
    return render(request, 'products/products_shop.template.html', {
        'products': products,
        'search_form': search_form
    })


def view_single_product(request, product_id):
    # return HttpResponse("Welcome to Products App")
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product.template.html', {
        'product': product
    })
