from flask import request, abort
from functools import wraps

roles = {
    "Casting Assistant": ["view:actors", "view:movies"],
    "Casting Director": ["view:actors", "view:movies", "modify:actors", "delete:actors"],
    "Executive Producer": ["view:actors", "view:movies", "modify:actors", "delete:actors", "add:movies", "delete:movies"]
}

def requires_permission(permission):
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            role = request.headers.get('Role')  # Example for simplicity
            if not role or permission not in roles.get(role, []):
                abort(403)
            return f(*args, **kwargs)
        return decorated
    return wrapper
