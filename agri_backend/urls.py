from django.contrib import admin
from django.urls import include, path
from authentication import urls as authentication_urls
from users import urls as urser_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(authentication_urls)),
    path('urer/', include(urser_urls)),
]
