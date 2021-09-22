from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
import jwt
from .models import *

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


class TheShow(APIView):
    def get(self, request, showID):
        try:
            theShow = Show.objects.filter(id=showID)[0]
            thatShow = {
                "id": theShow.id,
                "name": theShow.name,
                "imageLink": theShow.imageLink,
                "rating": theShow.rating
            }
            episodesOfTheShow = Episode.objects.filter(show = theShow)
            requiredEpisodes = []
            for epi in episodesOfTheShow:
                theEpisode = {
                    "show":epi.show.id,
                    "name":epi.name,
                    "episodeNumber":epi.episodeNumber,
                }
                requiredEpisodes.append(theEpisode)
            return Response({"show": thatShow, "episodes": requiredEpisodes})
        except:
            return Response({"status": "404 Not Found", "message": "Show does not exist."})

# TheEpisodeData - episodeID
# All the Comments
# All the replies to those comments
class TheEpisodeData(APIView):
    def get(self, request, episodeID):
        try:
            theEpisode = Episode.objects.filter(id=episodeID)[0]
            theComments = Comment.objects.filter(id=episodeID)
            thatEpisode = {
                    "id":theEpisode.id,
                    "show":theEpisode.show.id,
                    "name":theEpisode.name,
                    "episodeNumber":theEpisode.episodeNumber,
                }
            requiredComments = []
            for comment in theComments:
                theComment = {
                        "id": comment.id,
                        "user": {
                            "username": comment.user.username,
                            "email": comment.user.email,
                            "firstname": comment.user.first_name,
                            "lastname": comment.user.last_name,
                        },
                        "text": comment.text,
                        "episode":comment.episode.id,
                    }
                repliesToThisComment = Reply.objects.filter(comment=comment)
                allReplies = []
                for reply in repliesToThisComment:
                    theReply = {
                        "text":reply.text,
                        "comment":reply.comment.id,
                        "user": {
                            "username": reply.user.username,
                            "email": reply.user.email,
                            "firstname": reply.user.first_name,
                            "lastname": reply.user.last_name,
                        },
                    }
                    allReplies.append(theReply)
                theComment["replies"] = allReplies
                requiredComments.append(theComment)
            return Response({"episode":thatEpisode,"comments":requiredComments})
        except:
            return Response({"status": "404 Not Found", "message": "Episode does not exist."})

#http://localhost:8000/api/episode/1