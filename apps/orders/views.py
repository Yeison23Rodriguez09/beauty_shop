# beauty_shop\apps\orders\views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Order, OrderItem
from apps.cart.services import CartService
from apps.catalog.models import Product
from apps.orders.tasks import send_order_confirmation_email  # Opcional si usas Celery


class OrderListView(LoginRequiredMixin, View):
    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'orders/order_list.html', {'orders': orders})


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk, user=request.user)
        return render(request, 'orders/order_detail.html', {'order': order})


class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        cart = CartService(request)
        cart_items = list(cart.get_items())

        if not cart_items:
            messages.error(request, "Tu carrito está vacío.")
            return redirect('catalog:lista_productos')

        total_general = cart.get_total_price()

        return render(request, 'orders/order_confirm.html', {
            'cart_items': cart_items,
            'total_general': total_general
        })

    def post(self, request):
        cart = CartService(request)
        cart_items = list(cart.get_items())

        if not cart_items:
            messages.error(request, "Tu carrito está vacío.")
            return redirect('catalog:lista_productos')

        # Crear pedido
        order = Order.objects.create(
            user=request.user,
            total_price=cart.get_total_price(),
            status='pending',
        )

        # Crear ítems del pedido
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['product'].price
            )

        cart.clear()
        messages.success(request, "Tu pedido ha sido creado exitosamente.")

        # ✅ Enviar correo de confirmación (si Celery está activo)
        send_order_confirmation_email.delay(order.id)

        return redirect('orders:order_detail', pk=order.pk)
