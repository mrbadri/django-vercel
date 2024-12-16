from django.urls import path

from example.views import ProductListCreateView, index


urlpatterns = [
    path('', index),
    path('api/products/', ProductListCreateView.as_view(), name='product-list'),
]