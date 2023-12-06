import datetime
import hashlib
import os
import binascii
from django.utils import timezone
from django.db import models
from model_utils.models import TimeStampedModel

class User(TimeStampedModel):
    # Define language choices
    ENGLISH = 'EN'
    KANNADA = 'KA'
    LANGUAGE_CHOICES = [
        (ENGLISH, 'English'),
        (KANNADA, 'Kannada'),
    ]

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    name = models.CharField(max_length=100)
    photo_url = models.URLField()
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default=ENGLISH)

    def __str__(self):
        return self.name



class ExpiringToken(TimeStampedModel):
    TOKEN_EXPIRATION_TIME = datetime.timedelta(days=30)

    key = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'key')

    def expired(self):
        now = timezone.now()
        return self.last_updated < (now - self.TOKEN_EXPIRATION_TIME)

    def save(self, *args, **kwargs):
        if not self.key or self.expired():
            self.key = self.generate_key()
        return super(ExpiringToken, self).save(*args, **kwargs)

    def generate_key(self):
        unique_input = (
            'agri' + 
            str(self.user.id) + 
            str(datetime.datetime.now()) + 
            binascii.hexlify(os.urandom(20)).decode()
        )
        return hashlib.sha224(unique_input.encode('utf-8')).hexdigest()
    
    @classmethod
    def get_or_create_token(cls, user):
        token, _ = cls.objects.get_or_create(user=user)
        if token.expired():
            token.save()  
        return token

    def __str__(self):
        return str(self.key)

