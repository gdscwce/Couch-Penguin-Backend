from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.core.validators import MaxValueValidator
from django.utils import timezone

# Create your models here.
class Show(models.Model):
    name = models.CharField(max_length=250)
    imageLink = models.URLField(max_length=10000)
    rating = models.IntegerField()

    def __str__(self):
        return self.name

class Episode(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    episodeNumber = models.IntegerField()

    def __str__(self):
        return f"{self.episodeNumber}.{self.name}"

# Comment - who has commented - on what episode
# Reply - who has commented - on what comment
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)
    episode = models.ForeignKey(Episode,on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text