from django.urls import path
from .views import product_list_view, product_delete_view, product_create_view, product_detail_view, dynamic_lookup_view


app_name = 'products'

urlpatterns = [
    path('', product_list_view),
    path('<int:id>/', dynamic_lookup_view, name="product-detail"),
    path('<int:id>/delete/', product_delete_view),
]
