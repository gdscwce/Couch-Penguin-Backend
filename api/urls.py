from .views import *
from django.urls import path, include

urlpatterns = [
    path('api/hi', Hello.as_view(), name='Hello'),
    path('api/shows', Shows.as_view(), name='Shows')
]