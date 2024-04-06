from typing import TypedDict
from rest_framework_simplejwt.tokens import RefreshToken

from core.user.models import User

class Token(TypedDict):
    refresh: str
    access: str

def get_tokens_for_user(user: User) -> Token:
    refresh = RefreshToken.for_user(user)

    refresh['user_implicit_id'] = user.implicit_id

    return refresh