# beauty_shop/apps/payments/urls.py

from django.urls import path
from .views import CreateCheckoutSessionView, StripeWebhookView

app_name = 'payments'

urlpatterns = [
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
    path('webhook/', StripeWebhookView.as_view(), name='stripe_webhook'),
]
