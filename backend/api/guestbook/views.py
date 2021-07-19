from rest_framework import viewsets
from django.http import Http404
from .serializers import NoteSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, decorators
from .models import UserUpVote, UserDownVote, Note
from django.contrib.auth.models import User


# Create your views here.

class NoteCreateView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializers


class NoteUpdateView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializers

    @action(detail=False, methods=['POST'])
    def up_vote(self, request, pk=None):
        if UserUpVote.objects.filter(user_id=request.data['user_id'], note_id=request.data['note_id']).exists():
            raise Http404('you have made the up vote before')
        else:
            note = Note.objects.get(id=request.data['note_id'])
            note.up_vote += 1
            note.save()
            UserUpVote.objects.create(user_id=request.data['user_id'], note_id=request.data['note_id'])
            return Response('you have made the up vote update successfully')

    @action(detail=False, methods=['POST'])
    def down_vote(self, request, pk=None):
        if UserDownVote.objects.filter(user_id=request.data['user_id'], note_id=request.data['note_id']).exists():
            raise Http404('you have made the up vote before')
        else:
            note = Note.objects.get(id=request.data['note_id'])
            note.down_vote += 1
            note.save()
            UserDownVote.objects.create(user_id=request.data['user_id'], note_id=request.data['note_id'])
            return Response('you have made the down vote update successfully')


class UserCreateView(viewsets.ViewSet):
    @action(detail=False, methods=['POST'])
    def user_create_handler(self, request, pk=None):
        User.objects.create_user(username=request.data['username'], password=request.data['password'])
        return Response('You have successfully created user')

#
# def notes_list(request):
#     if request.method == 'GET':
#         notes = Note.objects.all()
#         serializer = NoteSerializers(notes, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         # to check if the post data is valid.
#         serializer = NoteSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
