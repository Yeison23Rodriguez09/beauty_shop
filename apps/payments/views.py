# beauty_shop/apps/payments/views.py
import json
import stripe
from django.conf import settings
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from apps.orders.models import Order
from apps.payments.stripe import create_checkout_session, handle_checkout_session_completed


class CreateCheckoutSessionView(View):
    """
    Crea una sesión de pago de Stripe para una orden específica.
    Espera un parámetro 'order_id' en el cuerpo POST.
    """

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            order_id = data.get('order_id')

            if not order_id:
                return JsonResponse({'error': 'ID de orden no proporcionado.'}, status=400)

            order = Order.objects.get(id=order_id)
            session_id = create_checkout_session(order)

            return JsonResponse({'session_id': session_id})

        except Order.DoesNotExist:
            return JsonResponse({'error': 'Orden no encontrada.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class StripeWebhookView(View):
    """
    Recibe y procesa webhooks enviados por Stripe.
    Valida la firma del evento y maneja eventos importantes como 'checkout.session.completed'.
    """

    def post(self, request, *args, **kwargs):
        payload = request.body
        sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
        endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError as e:
            # Cuerpo inválido
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            # Firma inválida
            return HttpResponse(status=400)

        # Procesar evento
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            handle_checkout_session_completed(session)

        return HttpResponse(status=200)
