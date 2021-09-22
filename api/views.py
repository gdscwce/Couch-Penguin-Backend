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
class Episodes(APIView):
    def get(self, request, ShowID):
        allEpisodes = Episodes.objects.filter(show=ShowID)
        allTheEpisodes = []
        for theEpisode in allEpisodes:
            thatEpisode = {
                "id": theEpisode.id,
                "name": theEpisode.name,
                "episodeNumber": theEpisode.episodeNumber,
            }
            allTheEpisodes.append(thatEpisode)
        return Response(allTheEpisodes)
# Get a particular Show


class theShow(APIView):
    def get(self, request, ShowID):
        # show_req = Shows.objects.filter(ShowID=ShowID)[0]
        return Shows.objects.filter(id=ShowID)

   
# Get a particular Episode - all its comments and replies
class theEpisode(APIView):
    def get(self,request,EpisodeID):
        return 

# Add a comment to an episode (Post)

class Comment(APIView):
    def post(self,request,EpisodeID,user):
        theComment = Comment.objects.filter(user=user)
        resp = {
            "user":Comment.user,

        }

# Add a reply to a comment (Post)

# Delete a comment (delete)
# Delete a reply

# Update a comment (put)
# Update reply
