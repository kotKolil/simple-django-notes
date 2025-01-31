from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Note
from .serializers import *

class NotesAPIView(APIView):

    def get(self, request, *args, **kwargs):
        NoteId = request.GET.get("id")
        Notes = Note.objects.all()
        notes = Notes.filter(Id = NoteId) & Notes.filter(personal != "personal")
        serializer = NotesSerializer(notes, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)