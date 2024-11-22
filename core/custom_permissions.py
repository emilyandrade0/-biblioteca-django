from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Permite apenas ao colecionador modificar a coleção.
    Outros usuários podem apenas visualizar.
    """
    def has_object_permission(self, request, view, obj):
        # Permitir métodos seguros (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True

        # Apenas o colecionador pode editar ou excluir
        return obj.colecionador == request.user
