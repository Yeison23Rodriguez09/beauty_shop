# beauty_shop/apps/core/views.py
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from django.utils.html import strip_tags


class HomeView(View):
    def get(self, request):
        return render(request, 'core/home.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'core/about.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'core/contact.html')

    def post(self, request):
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if not name or not email or not message:
            messages.error(request, "Por favor, completa todos los campos.")
            return redirect('core:contact')

        subject = f"Mensaje de contacto de {name}"
        clean_message = strip_tags(message)

        try:
            send_mail(
                subject=subject,
                message=clean_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[getattr(settings, 'CONTACT_EMAIL', settings.DEFAULT_FROM_EMAIL)],
                fail_silently=False,
            )
            messages.success(request, "Gracias por contactarnos. Te responderemos pronto.")
        except BadHeaderError:
            messages.error(request, "Encabezado inválido detectado.")
        except Exception as e:
            messages.error(request, "Error al enviar el mensaje. Intenta más tarde.")

        return redirect('core:contact')


# --- OPCIONAL ---
# Vista para monitoreo de estado del sistema
class HealthCheckView(View):
    def get(self, request):
        return HttpResponse("OK", content_type="text/plain")


# Vista para modo mantenimiento
class MaintenanceView(View):
    def get(self, request):
        return render(request, 'core/maintenance.html', status=503)
