from rest_framework import permissions
import ipaddress

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return getattr(obj , 'owner' ,  getattr(obj, 'user' , None )) == request.user

class IsAdminRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated
            and getattr(request.user , 'role' , None) == 'admin'
        )

class IsStaffRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated
            and getattr(request.user , 'role' , None) in ['admin' , 'staff']
        )

class IsRegularUserRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

class RestricFieldAccessInformation(permissions.BasePermission):

    def has_permission(self, request, view):

        if not request.user or not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS or getattr(request.user
                                                                 , 'role', None) in ['admin' , 'staff']:
            return True

        data = request.data
        if any(field in data for field in self.RESTRICTED_FIELDS):
            return False

        return True

class IPWatchListPermissions(permissions.BasePermission):
    ALLOWED_IPS = ['127.0.0.1' , '192.168.1.100']

    def get_client_ip(self, request):
        x_forwarded_for  = request.Meta.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()

        else:
            ip = request.Meta.get('REMOTE_ADDR')

        return ip

    def has_permission(self, request, view):
        ip = self.get_client_ip(request)
        return ip in self.ALLOWED_IPS

class ReadOnlyOrStaffPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(
                request.user and request.user.is_authenticated
                and getattr(request.user , 'role' , None) in ['admin' , 'staff']
            )