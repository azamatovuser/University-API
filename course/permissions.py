from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author.user


class IsTeacherOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user.profile.role)
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.profile.role == 1