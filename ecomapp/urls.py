from django.urls import include, path
from ecomapp.views import base_view, category_view, product_view


urlpatterns = [
    path('category/<str:category_slug>/', category_view, name='category_detail'),
    path('product/<str:product_slug>/', product_view, name='product_detail'),
    path('', base_view, name='base'),
]
