from django.shortcuts import render

from .models import Product

def product_detail(request):
    return render(request, 'storeitems/product_detail.html')
