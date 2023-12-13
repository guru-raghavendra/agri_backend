from django.urls import path
from .views import GoogleAuthView, TokenRegenerationView

urlpatterns = [
    path('google/', GoogleAuthView.as_view(), name='google_auth'),
    path('regenerate-token/', TokenRegenerationView.as_view(), name='regenerate-token'),
]
