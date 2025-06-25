# beauty_shop\config\settings\development.py
from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

# ========================
# ⚙️ Django Allauth Config (modo moderno solo email)
# ========================

ACCOUNT_AUTHENTICATION_METHOD = "email"         # Solo login por email
ACCOUNT_USERNAME_REQUIRED = False               # No se requiere username
ACCOUNT_EMAIL_REQUIRED = True                   # Email obligatorio
ACCOUNT_SIGNUP_FIELDS = ["email"]               # Solo se solicita email (password lo maneja Allauth)

ACCOUNT_EMAIL_VERIFICATION = "none"             # "mandatory" para producción con SMTP real
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

SITE_ID = 1

# Stripe Settings (usa tus claves reales si ya tienes cuenta)
STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY", "pk_test_1234567890")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "sk_test_1234567890")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "whsec_test_1234567890")
