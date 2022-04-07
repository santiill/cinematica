from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.admin == request.user


class IsAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated)