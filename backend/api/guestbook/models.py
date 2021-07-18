from django.db import models

# Create your models here.


class Note(models.Model):
    content = models.TextField()
    upvote = models.BigIntegerField(default=0)
    downvote = models.BigIntegerField(default=0)

