from django.urls import path

from . import views

urlspatterns = [
    path('storeitems/', views.product_detail, name='product_detail')
]