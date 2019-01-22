from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """"
    Custom permission class to only allow owners of object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class IsOwnerOrReadOnlyFile(IsOwnerOrReadOnly):
    def has_object_permission(self, request, view, obj):
        obj.owner = obj.exam.owner
        return super(IsOwnerOrReadOnlyFile, self).has_object_permission(request=request,
                                                                        view=view,
                                                                        obj=obj)
