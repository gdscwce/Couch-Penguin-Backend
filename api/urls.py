from .views import *
from django.urls import path, include

urlpatterns = [
    path('api/hi', Hello.as_view(), name='Hello'),
]