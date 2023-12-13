
from google.oauth2 import id_token
from google.auth.transport import requests
from authentication.models import ExpiringToken
from users.models import User

def decode_google_token(token, client_id):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)
        mail = idinfo['email'] 

        user, _ = User.objects.get_or_create(email=mail, defaults={
            'email': idinfo.get('email'),
            'name': idinfo.get('name'),
            'photo_url': idinfo.get('picture'),
        })

        token = ExpiringToken.get_or_create_token(user)
        return token.key

    except ValueError:
        return 'INVALID'