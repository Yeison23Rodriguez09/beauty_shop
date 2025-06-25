# beauty_shop/config/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

# ========================
# ⚙️ Selección del entorno
# ========================
# Usa la variable de entorno DJANGO_ENV para elegir el settings adecuado
django_env = os.getenv('DJANGO_ENV', 'development').lower()

if django_env == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

# ========================
# 🚀 Aplicación WSGI
# ========================
application = get_wsgi_application()
