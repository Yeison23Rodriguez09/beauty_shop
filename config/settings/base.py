# beauty_shop\config\settings\base.py
import os
import dj_database_url
from pathlib import Path

# Base directory del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ========================
# 🔐 Configuración general
# ========================
SECRET_KEY = os.getenv('SECRET_KEY', 'clave-secreta-desarrollo')
DEBUG = False
ALLOWED_HOSTS = []

# ========================
# 🧩 Aplicaciones instaladas
# ========================
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Terceros
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_celery_results',

    # Locales
    'apps.core',
    'apps.users',
    'apps.catalog',
    'apps.cart',
    'apps.orders',
    'apps.payments',
    'apps.blog',
    'apps.credits',
    'apps.importer',
]

# ========================
# 🧠 Middleware
# ========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ========================
# 📦 Configuración básica
# ========================
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True
SITE_ID = 1
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ========================
# 🗂️ Templates
# ========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ========================
# 🔐 Password validators
# ========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ========================
# 📁 Archivos estáticos y media
# ========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 📂 Subcarpetas importantes
PRODUCT_EXPORT_PATH = MEDIA_ROOT / 'exports'
PRODUCT_EXPORT_PATH.mkdir(parents=True, exist_ok=True)
PRODUCT_IMAGE_FOLDER = MEDIA_ROOT / 'img'
PRODUCT_IMAGE_FOLDER.mkdir(parents=True, exist_ok=True)

# ========================
# 📧 Email base (sobrescribir en entorno)
# ========================
DEFAULT_FROM_EMAIL = "admin@beautyshop.com"
SERVER_EMAIL = "admin@beautyshop.com"

# ========================
# 🌐 REST Framework
# ========================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

# ========================
# 🗄️ Configuración de Base de Datos
# ========================
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3'),
        conn_max_age=600
    )
}

# 🛒 Identificador para el carrito de compras en la sesión
CART_SESSION_ID = 'cart'