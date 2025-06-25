# beauty_shop/apps/cart/urls.py
from django.urls import path
from .views import (
    CartDetailView,
    AddToCartView,
    RemoveFromCartView,
    ClearCartView,
)

app_name = 'cart'

urlpatterns = [
    # 🛒 Vista del carrito
    path('', CartDetailView.as_view(), name='cart_detail'),

    # ➕ Agregar producto al carrito
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),

    # ❌ Eliminar producto del carrito
    path('remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),

    # 🧹 Vaciar el carrito
    path('clear/', ClearCartView.as_view(), name='clear_cart'),
]
