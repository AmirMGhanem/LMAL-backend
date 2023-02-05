from functools import wraps
from fastapi import Header
from app.settings import *
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = Header.headers.get('token')
        if not token:
            return {"Token is missing", 403}
        else:
            try:
                data = jwt.decode(token, key=SECRET_KEY, algorithms=["HS256"])
            except:
                return custom_error("Unauthenticated", 401)
            return f(*args, **kwargs)

    return decorated

