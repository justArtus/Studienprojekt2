from django.shortcuts import render

from storeitems.models import Product

def frontpage(request):
    products = Product.objects.all()[0:6]
    return render(request, 'store/frontpage.html', {
        'products': products
    })


