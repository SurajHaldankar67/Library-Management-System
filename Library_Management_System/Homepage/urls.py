from django.urls import path
from .views import Homepage_view

urlpatterns = [
    path("", Homepage_view),
]