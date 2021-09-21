from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
import jwt
from .models import *

# Create your views here.
class Hello(APIView):
    def get(self, request):
        return Response({"message": "Hello World"})

class Shows(APIView):
    def get(self, request):
        allShows = Show.objects.all()
        allTheShows = []
        for theShow in allShows:
            thatShow = {
                "id": theShow.id,
                "name": theShow.name,
                "imageLink": theShow.imageLink,
                "rating": theShow.rating
            }
            allTheShows.append(thatShow)
        return Response(allTheShows)


# All episodes of a show

# Get a particular Show
# Get a particular Episode - all its comments and replies

#Add a comment to an episode (Post)
# Add a reply to a comment (Post)

# Delete a comment (delete)
# Delete a reply

# Update a comment (put)
# Update reply


