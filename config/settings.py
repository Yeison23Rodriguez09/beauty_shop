# beauty_shop\config\settings.py
import os
from pathlib import Path

# Base directory del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Determina el entorno de Django (development, production, testing, etc.)
DJANGO_ENV = os.getenv('DJANGO_ENV', 'development').lower()

# ====================================================
# 📁 Archivos estáticos y multimedia
# ====================================================

# Archivos multimedia (subidos por el usuario)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Carpeta donde vivirá el Excel del catálogo
PRODUCT_EXPORT_PATH = MEDIA_ROOT / 'exports'
PRODUCT_EXPORT_PATH.mkdir(parents=True, exist_ok=True)

# Carpeta base para imágenes de productos
PRODUCT_IMAGE_FOLDER = MEDIA_ROOT / 'img'
PRODUCT_IMAGE_FOLDER.mkdir(parents=True, exist_ok=True)

# ====================================================
# 📬 Correo del administrador (para errores, formularios, etc.)
# ====================================================
ADMINS = [
    ("Andrey Yei", "admin@beautyshop.com"),
]

DEFAULT_FROM_EMAIL = "admin@beautyshop.com"
SERVER_EMAIL = "admin@beautyshop.com"

# Email backend (ejemplo con consola, cambiar en producción)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ====================================================
# 🔁 Carga de configuración según entorno
# ====================================================
if DJANGO_ENV == 'production':
    from .settings.production import *
elif DJANGO_ENV == 'development':
    from .settings.development import *
else:
    raise ValueError(f"DJANGO_ENV no válido: '{DJANGO_ENV}'. Debe ser 'development' o 'production'.")
