from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
import jwt

# Create your views here.
class Hello(APIView):
    def get(self, request):
        return JsonResponse({"message": "Hello World"})
