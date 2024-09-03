from .exceptions import PermissionDenied

def validate_permissions(user):
    if not user.has_perm('crm_app.can_manage_users'):
        raise PermissionDenied('The user has no authorization to see this resource.')