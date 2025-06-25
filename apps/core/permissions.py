# beauty_shop\apps\core\permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Permite acceso de lectura (GET, HEAD, OPTIONS) a cualquiera,
    pero solo los admin pueden hacer POST, PUT, DELETE.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsOwnerOrReadOnly(BasePermission):
    """
    El usuario puede ver cualquier objeto,
    pero solo modificar o eliminar si es el dueño (owner).
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsCustomer(BasePermission):
    """
    Permite el acceso solo si el usuario tiene rol 'customer'.
    Requiere que el modelo de usuario tenga un campo `role`.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'role', None) == 'customer'
