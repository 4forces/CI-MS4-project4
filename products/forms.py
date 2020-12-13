from django import forms
from .models import Product, Category

class SearchForm(forms.Form):
    name = forms.CharField(max_length=150, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      required=False)
