from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from authentication.models import ExpiringToken

class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token_key = request.headers.get('Authorization')
        if not token_key:
            # return None  
            raise AuthenticationFailed('Token not present')
        try:
            token = ExpiringToken.objects.get(key=token_key)
            if token.expired():
                raise AuthenticationFailed('Token has expired')
            # token.user.is_authenticated = True
            return (token.user, token)  # Authentication successful
        except ExpiringToken.DoesNotExist:
            raise AuthenticationFailed('Invalid token')
    
    def authenticate_header(self, request):
        return 'Token'
