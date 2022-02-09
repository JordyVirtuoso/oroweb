# from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    # link urls.py in oro/api folder
    path('api/', include('oro.api.urls')),
    path('', views.index)
]