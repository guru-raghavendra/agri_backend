# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .token_decoder import decode_google_token

class GoogleAuthView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        client_id = '44319179088-ih4r7b6jo25m4epblohftuu019gfur6g.apps.googleusercontent.com'

        token = decode_google_token(token, client_id)
        if token != 'INVALID':
            return Response({'message': 'success', 'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Please try logging after sometime'}, status=status.HTTP_400_BAD_REQUEST)
