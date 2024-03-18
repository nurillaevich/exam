from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()


def jwt_payload_handler(user: User):
    refresh = RefreshToken.for_user(user)

    tokens = {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }
