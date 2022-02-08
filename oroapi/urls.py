from django import urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # link urls.py in oro folder
    path('', include('oro.urls')),
    # paths to login with rest_framework's urls
    path('api-auth/', include('rest_framework.urls'))
]
