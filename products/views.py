from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import SearchForm, ProductForm, CategoryForm, SupplierForm
from django.contrib import messages


# Create your views here.
# 'READ' functions
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


# 'CREATE' functions
@login_required
def create_product(request):
    if request.method == 'POST':
        create_form = ProductForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            messages.success(request, f"Product "
                             f"{create_form.cleaned_data['name']} created")
            return redirect(reverse(create_product))
        else:
            return render(request, 'products/product_create.template.html', {
                'form': create_form
            })
    else:
        create_form = ProductForm()
        return render(request, 'products/product_create.template.html', {
            'form': create_form
        })


@login_required
def create_category(request):
    if request.method == 'POST':
        create_form = CategoryForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(create_category))
        else:
            return render(request, 'products/category_create.template.html', {
                'form': create_form
            })
    else:
        create_form = CategoryForm()
        return render(request, 'products/category_create.template.html', {
                'form': create_form
        })


@login_required
def create_supplier(request):
    if request.method == 'POST':
        create_form = SupplierForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(create_supplier))
        else:
            return render(request, 'products/supplier_create.template.html', {
                'form': create_form
            })
    else:
        create_form = SupplierForm()
        return render(request, 'products/supplier_create.template.html', {
                'form': create_form
        })


# 'UPDATE' functions
@login_required
def update_product(request, product_id):
    # Retrieves the product
    product_updating = get_object_or_404(Product, pk=product_id)
    # Check for 'POST'
    if request.method == 'POST':
        update_form = ProductForm(request.POST, instance=product_updating)
        if update_form.is_valid():
            update_form.save()
            return redirect(reverse(view_shop))
        else:
            return render(request, 'products/product_update.template.html', {
                "form": update_form
            })
    # Creates the product_form and populate it with product_updating fields
    else:
        update_form = ProductForm(instance=product_updating)
        return render(request, 'products/product_update.template.html', {
            "form": update_form
        })


# 'DELETE' functions
@login_required
def delete_product(request, product_id):
    product_deletion = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_deletion.delete()
        return redirect(view_shop)
    else:
        return render(request, 'products/product_delete.template.html', {
            "product": product_deletion
        })
