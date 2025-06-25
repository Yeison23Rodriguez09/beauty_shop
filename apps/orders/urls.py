# beauty_shop/apps/orders/urls.py
from django.urls import path
from .views import OrderListView, OrderDetailView, OrderCreateView

app_name = 'orders'

urlpatterns = [
    # --- Gestión de pedidos ---
    path('', OrderListView.as_view(), name='order_list'),           # Lista de pedidos del usuario
    path('<int:pk>/', OrderDetailView.as_view(), name='order_detail'),  # Detalle de un pedido
    path('crear/', OrderCreateView.as_view(), name='order_create'),     # Crear nuevo pedido desde el carrito
]
