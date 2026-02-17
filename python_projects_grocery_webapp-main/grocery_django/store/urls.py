from django.urls import path
from . import views

urlpatterns = [
    path('getUOM', views.get_uom, name='get_uom'),
    path('getProducts', views.get_products, name='get_products'),
    path('insertProduct', views.insert_product, name='insert_product'),
    path('deleteProduct', views.delete_product, name='delete_product'),
    path('getAllOrders', views.get_all_orders, name='get_all_orders'),
    path('insertOrder', views.insert_order, name='insert_order'),
]
