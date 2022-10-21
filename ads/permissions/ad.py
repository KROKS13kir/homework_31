from rest_framework.permissions import BasePermission
from users.models import UserRoles


class IsCreatedAdminModer(BasePermission):
    message = 'Only user who created the ad, amdin and moderators could modify or delete it.'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or request.user.role in [UserRoles.MODERATOR, UserRoles.ADMIN]:
            return True
        return False
