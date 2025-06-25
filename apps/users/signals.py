# beauty_shop\apps\users\signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

@receiver(post_save, sender=User)
def assign_default_group(sender, instance, created, **kwargs):
    """
    Asigna automáticamente un grupo por defecto a los usuarios nuevos según su rol.
    """
    if created:
        if instance.role == User.Role.CUSTOMER:
            group_name = 'Clientes'
        elif instance.role == User.Role.ADMIN:
            group_name = 'Administradores'
        else:
            group_name = None

        if group_name:
            group, _ = Group.objects.get_or_create(name=group_name)
            instance.groups.add(group)

        # Puedes agregar más lógica para permisos personalizados aquí

        # Guardar el usuario con el grupo asignado
        instance.save()
