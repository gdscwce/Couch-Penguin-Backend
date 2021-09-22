from .views import *
from django.urls import path, include

urlpatterns = [
    path('api/shows', Shows.as_view(), name='Shows'),
    path('api/show/<int:showID>', TheShow.as_view(), name="TheShow"),
    path('api/episode/<int:episodeID>',TheEpisodeData.as_view(),name="TheEpisode"),
]