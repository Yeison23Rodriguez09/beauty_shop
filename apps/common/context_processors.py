# beauty_shop\apps\common\context_processors.py
from apps.catalog.models import Category
from django.conf import settings


def categories_processor(request):
    """
    Hace disponibles todas las categorías en todas las plantillas.
    Útil para menús o filtros globales.
    """
    categories = Category.objects.all()
    return {'menu_categories': categories}


def cart_session_id(request):
    """
    Devuelve el ID de sesión del carrito, configurable desde settings.
    """
    return {'CART_SESSION_ID': getattr(settings, 'CART_SESSION_ID', 'cart')}
