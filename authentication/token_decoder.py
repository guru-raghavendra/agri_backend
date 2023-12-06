
from google.oauth2 import id_token
from google.auth.transport import requests

from users.models import ExpiringToken, User

def decode_google_token(token, client_id):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)
        mail = idinfo['email'] 

        user, created = User.objects.get_or_create(email=mail, defaults={
            'email': idinfo.get('email'),
            'name': idinfo.get('name'),
            'photo_url': idinfo.get('picture'),
        })

        token = ExpiringToken.get_or_create_token(user)
        return token.key

    except ValueError:
        return 'INVALID'



    """
    {'iss': 'https://accounts.google.com', 
    'azp': '44319179088-ih4r7b6jo25m4epblohftuu019gfur6g.apps.googleusercontent.com',
    'aud': '44319179088-ih4r7b6jo25m4epblohftuu019gfur6g.apps.googleusercontent.com', 
    'sub': '101399478297349005446', 'email': 'h.guru.raghavendra@gmail.com', 
    'email_verified': True, 'nbf': 1701885094, 'name': 'Guru raghavendra',
    'picture': 'https://lh3.googleusercontent.com/a/ACg8ocJcbOtAxcIOxKubZifceCldR16QR-deSfb3O2wuKFQu=s96-c', 
    'given_name': 'Guru raghavendra', 'locale': 'en', 'iat': 1701885394, 'exp': 1701888994,
    'jti': '81b4c05b81e073c3a477132ce3548ca7987b1190'}
[06/Dec/2023 17:56:50] "POST /auth/google/ HTTP/1.1" 200 61
    """