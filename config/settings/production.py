# beauty_shop/config/settings/production.py
import os
import dj_database_url
from .base import *

DEBUG = False

# Allowed hosts (Render proporciona el dominio por defecto)
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'beauty-shop.onrender.com').split(',')
if not any(ALLOWED_HOSTS):
    raise ValueError("DJANGO_ALLOWED_HOSTS no está definido correctamente.")

# Redirección después del login para evitar error 404 en /accounts/profile/
LOGIN_REDIRECT_URL = '/'

# Configuración de la base de datos (Render proporciona DATABASE_URL)
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

# Archivos estáticos y media
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# WhiteNoise para servir archivos estáticos en producción
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuración del correo (SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)

if not EMAIL_HOST_USER or not EMAIL_HOST_PASSWORD:
    raise ValueError("EMAIL_HOST_USER y EMAIL_HOST_PASSWORD deben estar definidos.")

# Seguridad
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# CORS (maneja valores vacíos sin lanzar error)
CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', '')
if CORS_ALLOWED_ORIGINS:
    CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS.split(',')
else:
    CORS_ALLOWED_ORIGINS = []
