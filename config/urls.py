# beauty_shop/config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view as get_yasg_schema_view
from drf_yasg import openapi

# ========================
# 🔗 Documentación y Esquema API
# ========================
yasg_schema_view = get_yasg_schema_view(
    openapi.Info(
        title="Beauty Shop API",
        default_version='v1',
        description="Documentación interactiva para la API de Beauty Shop",
        contact=openapi.Contact(email="admin@beautyshop.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_urlpatterns = [
    path(
        'schema/',
        get_schema_view(
            title="Beauty Shop API",
            description="Esquema de la API para la tienda Beauty Shop"
        ),
        name='api-schema'
    ),
    path('docs/', yasg_schema_view.with_ui('swagger', cache_timeout=0), name='api-docs'),
    path('redoc/', yasg_schema_view.with_ui('redoc', cache_timeout=0), name='api-redoc'),
]

# ========================
# 🌐 Rutas principales
# ========================
urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Autenticación (Allauth)
    path('accounts/', include('allauth.urls')),

    # Apps locales con namespaces
    path('', include('apps.core.urls', namespace='core')),
    path('cuentas/', include('apps.users.urls', namespace='users')),
    path('productos/', include('apps.catalog.urls', namespace='catalog')),
    path('carrito/', include('apps.cart.urls', namespace='cart')),
    path('pedidos/', include('apps.orders.urls', namespace='orders')),
    path('pagos/', include('apps.payments.urls', namespace='payments')),
    path('blog/', include('apps.blog.urls', namespace='blog')),

    # Documentación de la API
    path('api/', include(api_urlpatterns)),
]

# ========================
# 🖼️ Archivos Media en desarrollo
# ========================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)