from rest_framework import serializers
from .models import Note


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'username', 'content', 'up_vote', 'down_vote')
