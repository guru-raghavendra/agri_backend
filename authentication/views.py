from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.models import ExpiringToken
from .token_decoder import decode_google_token

class GoogleAuthView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        client_id = '44319179088-ih4r7b6jo25m4epblohftuu019gfur6g.apps.googleusercontent.com'

        token = decode_google_token(token, client_id)
        if token != 'INVALID':
            return Response({'message': 'success', 'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Please try logging after sometime, invalid token'}, status=status.HTTP_400_BAD_REQUEST)

#may have to depricate this
class TokenRegenerationView(APIView):
    def put(self, request, *args, **kwargs):
        old_token_key = request.headers.get('Authorization')

        if not old_token_key:
            return Response({ "message" :"Token is required."}, status=status.HTTP_400_BAD_REQUEST)

        user = self.get_user_from_token(old_token_key)
        if not user:
            return Response({ "message" :"Invalid token or Token not expired"}, status=status.HTTP_401_UNAUTHORIZED)

        new_token = ExpiringToken.get_or_create_token(user)

        return Response({'message': 'success', 'token': new_token}, status=status.HTTP_200_OK)

    def get_user_from_token(self, token_key):
        try:
            token = ExpiringToken.objects.get(key=token_key)
            if token.expired():
                return token.user
            return None
        except ExpiringToken.DoesNotExist:
            return None
