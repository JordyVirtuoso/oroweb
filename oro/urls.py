# from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    # link urls.py in oro/api folder
    path('api/', include('oro.api.urls')),
]