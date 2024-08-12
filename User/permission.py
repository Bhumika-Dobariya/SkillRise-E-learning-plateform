

from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False
        

        return getattr(request.user, 'role', None) == 'Admin'

class IsInstructor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Instructor'

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Student'