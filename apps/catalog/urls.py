# beauty_shop/apps/catalog/urls.py
from django.urls import path
from .views import ProductListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='lista_productos'),  # <-- antes era 'productos/'

    path('categoria/<slug:category_slug>/', ProductListView.as_view(), name='product_by_category'),
    path('producto/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
