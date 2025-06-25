# beauty_shop/apps/cart/services.py
from decimal import Decimal
from django.conf import settings
from apps.catalog.models import Product


class CartService:
    """
    Servicio para manejar la lógica del carrito de compras
    basado en sesiones del usuario.
    """
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """
        Agrega un producto al carrito o actualiza su cantidad.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)  # Siempre string para serialización
            }

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        """
        Marca la sesión como modificada para que Django la guarde.
        """
        self.session.modified = True

    def remove(self, product):
        """
        Elimina un producto del carrito.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """
        Limpia completamente el carrito.
        """
        self.session[settings.CART_SESSION_ID] = {}
        self.save()

    def get_items(self):
        """
        Devuelve un generador con los productos del carrito enriquecidos con datos del catálogo.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            item = self.cart[str(product.id)]
            total_price = Decimal(item['price']) * item['quantity']

            yield {
                'product': product,
                'quantity': item['quantity'],
                'price': Decimal(item['price']),
                'total_price': total_price
            }

    def get_total_price(self):
        """
        Calcula el total del carrito.
        """
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values()
        )

    def __len__(self):
        """
        Permite usar len(carrito) para obtener la cantidad total de productos.
        """
        return sum(item['quantity'] for item in self.cart.values())
