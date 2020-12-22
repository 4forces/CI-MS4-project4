from django import forms
from .models import Product, Category, Supplier
from cloudinary.forms import CloudinaryJsFileField


class SearchForm(forms.Form):
    name = forms.CharField(max_length=150, required=False,
                           label="Search product by name")
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      required=False, label="Select Category")


class ProductForm(forms.ModelForm):
    cover = CloudinaryJsFileField()
    # 'meta' defines which model ('product') this form references
    class Meta:
        model = Product
        fields = ('name', 'cost', 'unit', 'quantity',
                  'category', 'part_number', 'desc',
                  'supplier', 'cover')


class CategoryForm(forms.ModelForm):
    # 'meta' defines which model ('product') this form references
    class Meta:
        model = Category
        fields = ('name',)


class SupplierForm(forms.ModelForm):
    # 'meta' defines which model ('product') this form references
    class Meta:
        model = Supplier
        fields = ('name', 'country',)
