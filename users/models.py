from django.db import models
from model_utils.models import TimeStampedModel

class User(TimeStampedModel):
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
    
    @property
    def is_authenticated(self):
        return True