from .views import *
from django.urls import path, include

urlpatterns = [
    path('api/shows', Shows.as_view(), name='Shows'),
    path('api/show/<int:showID>', TheShow.as_view(), name="TheShow"),
    path('api/episode/<int:episodeID>',TheEpisodeData.as_view(),name="TheEpisode"),
    path('api/reply/<int:commentID>/<str:username>',ReplyAPI.as_view(),name="ReplyAPI"),
    path('api/comment/<int:episodeID>/<str:username>', CommentAPI.as_view(), name="CommentAPI"),
    path('api/comment/<int:id>', theComment.as_view(), name="theComment"),
    path('api/reply/<int:id>', theReply.as_view(), name="theReply"),
    path('api/login',LoginAPI.as_view(),name="LoginAPI"),
    path('api/register',RegisterAPI.as_view(),name="RegisterAPI"),
    path('api/profile/<str:username>',ProfileAPI.as_view(),name="ProfileAPI"),


]