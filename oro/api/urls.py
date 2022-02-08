from django.urls import path, include
from .views import ItemApiView

urlpatterns = [
    # path to class based custom view by rest_framework
    path('', ItemApiView.as_view())
]