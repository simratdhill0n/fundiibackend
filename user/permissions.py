from rest_framework.permissions import BasePermission

class CreateUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True  # Allow unauthenticated access for POST
        return request.user and request.user.is_authenticated  # Require authentication for other methods