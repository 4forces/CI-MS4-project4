from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from .forms import SearchForm, ProductForm


# Create your views here.
def view_shop(request):
    # return HttpResponse("Welcome to Products App")
    products = Product.objects.all()
    search_form = SearchForm(request.GET)
    return render(request, 'products/products_view_shop.template.html', {
        'products': products,
        'search_form': search_form
    })


def view_single_product(request, product_id):
    # return HttpResponse("Welcome to Products App")
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_view_one.template.html', {
        'product': product
    })


def create_product(request):
    if request.method == 'POST':
        create_form = ProductForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(view_shop))
        else:
            return render(request, 'products/product_create.template.html', {
                'form': create_form
            })
    else:
        create_form = ProductForm()
        return render(request, 'products/product_create.template.html', {
            'form': create_form
        })
