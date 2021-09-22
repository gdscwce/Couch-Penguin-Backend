from django.db.models import deletion
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


class TheEpisodeData(APIView):
    def get(self, request, episodeID):
        try:
            theEpisode = Episode.objects.filter(id=episodeID)[0]
            theComments = Comment.objects.filter(episode=theEpisode)
            thatEpisode = {
                    "id":theEpisode.id,
                    "show":theEpisode.show.id,
                    "name":theEpisode.name,
                    "episodeNumber":theEpisode.episodeNumber,
                }
            requiredComments = []
            print("Length is"+str(len(theComments)))
            for comment in theComments:
                theComment = {
                        "id": comment.id,
                        "user": {
                            "username": comment.user.username,
                            "email": comment.user.email,
                            "first_name": comment.user.first_name,
                            "last_name": comment.user.last_name,
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
                print("Mera yassssuuuuu")
            return Response({"episode":thatEpisode,"comments":requiredComments})
        except:
            return Response({"status": "404 Not Found", "message": "Episode does not exist."})


class CommentAPI(APIView):
    def post(self, request, episodeID, username):
        
        try:
            thatEpisode = Episode.objects.filter(id=episodeID)[0]
        except:
            return Response({"status": "404 Not Found", "message": "Episode does not exist."})

        try:
            thatUser = User.objects.filter(username=username)[0]
        except:
            return Response({"status": "404 Not Found", "message": "Episode does not exist."})
        
        text = request.data['text']

        try:
            addComment = Comment(episode=thatEpisode, user=thatUser, text=text)
            addComment.save()
        except:
            return Response({"status": "500 Internal Server Error", "message": "database went through an error."})
        
        resp = {
                "id": addComment.id,
                "username": addComment.user.username,
                "text": addComment.text,
                "episodeID": addComment.episode.id,
                "status": "201 Created"
            }
        return Response(resp)


class ReplyAPI(APIView):
    def post(self,request,commentID,username):
        try:
            thatComment = Comment.objects.filter(id=commentID)[0]
        except:
            return Response({"status": "404 Not Found", "message": "Comment does not exist."})
        try:
            thatUser = User.objects.filter(username=username)[0]
        except:
            return Response({"status": "404 Not Found", "message": "Episode does not exist."})
        text = request.data["text"]
        try:
            addReply = Reply(comment=thatComment,user=thatUser,text=text)
            addReply.save()
        except:
            return Response({"status": "500 Internal Server Error", "message": "database went through an error."})
        resp = {
            "id": addReply.id,
            "username": addReply.user.username,
            "text": addReply.text,
            "commentID": addReply.comment.id,
            "status": "201 Created"
        }
        return Response(resp)


class theComment(APIView):
    def delete(self, request, id):
        comment = Comment.objects.filter(id=id)
        if comment:
            comment.delete()
            return Response({"status":"Comment deleted successfully"})
        return Response({"status": "404 Not Found", "message": "Comment does not exist."})
       
    
    def put(self, request, id):
        try:
            text = request.data["text"]
            comment = Comment.objects.filter(id=id).update(text=text)
            return Response({"status":"Comment Updated successfully"})
        except: 
            return Response({"status": "404 Not Found", "message": "Comment does not exist."})


class theReply(APIView):
    def delete(self, request, id):
        #Boooooooooo
        reply = Reply.objects.filter(id=id)
        if reply:
            reply.delete()
            return Response({"status":"Reply deleted successfully"})
        return Response({"status": "404 Not Found", "message": "Reply does not exist."})
        
    def put(self, request, id):
        try:
            text = request.data["text"]
            reply = Reply.objects.filter(id=id).update(text=text)
            return Response({"status":"Reply Updated successfully"})
        except: 
            return Response({"status": "404 Not Found", "message": "Reply does not exist."})