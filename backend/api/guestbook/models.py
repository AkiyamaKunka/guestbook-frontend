from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Note(models.Model):
    username = models.TextField(max_length=100, default='user_default_name')
    content = models.TextField(max_length=100)
    up_vote = models.BigIntegerField(default=0)
    down_vote = models.BigIntegerField(default=0)


class UserUpVote(models.Model):
    user_id = models.BigIntegerField(default=0)
    note_id = models.BigIntegerField(default=0)


class UserDownVote(models.Model):
    user_id = models.BigIntegerField(default=0)
    note_id = models.BigIntegerField(default=0)
