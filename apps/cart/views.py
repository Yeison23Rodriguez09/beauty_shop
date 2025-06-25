# beauty_shop/apps/cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from apps.catalog.models import Product
from .services import CartService


# ========================
# 🛒 Vista del carrito
# ========================
class CartDetailView(View):
    def get(self, request):
        cart = CartService(request)
        return render(request, 'cart/cart_detail.html', {
            'cart_items': cart.get_items(),
            'total_price': cart.get_total_price()
        })


# ========================
# ➕ Agregar producto
# ========================
class AddToCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        try:
            quantity = int(request.POST.get('quantity', 1))
        except (TypeError, ValueError):
            quantity = 1

        cart = CartService(request)
        cart.add(product, quantity)

        messages.success(request, f"'{product.name}' fue agregado al carrito.")
        return redirect('cart:cart_detail')


# ========================
# ❌ Eliminar producto
# ========================
class RemoveFromCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart = CartService(request)
        cart.remove(product)

        messages.info(request, f"'{product.name}' fue eliminado del carrito.")
        return redirect('cart:cart_detail')


# ========================
# 🧹 Vaciar el carrito
# ========================
class ClearCartView(View):
    def post(self, request):
        cart = CartService(request)
        cart.clear()
        messages.warning(request, "Tu carrito ha sido vaciado.")
        return redirect('cart:cart_detail')
