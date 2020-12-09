from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("Welcome to Products App")
    return render(request, 'products/products.template.html')
