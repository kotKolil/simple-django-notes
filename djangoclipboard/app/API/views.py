from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Note
from django.contrib.auth import get_user_model
from .serializers import *
from rest_framework.permissions import *
import json

class NotesAPIViewCommon(APIView):

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        note_id = request.GET.get("id")
        username =request.GET.get("username")

        if note_id and not username:
            # Start with all notes
            notes_query = Note.objects.all()

            # Filter by note ID if provided
            if note_id:
                notes_query = notes_query.filter(Id=note_id)

            # Exclude personal notes
            notes_query = notes_query.exclude(personal="personal")

            # Serialize the filtered notes
            serializer = NotesSerializer(notes_query, many=True)
            if serializer:
                return Response(serializer.data, status=status.HTTP_200_OK)
        elif not note_id and username:
            # Start with all notes
            notes_query = Note.objects.all()

            # Filter by note ID if provided
            if note_id:
                User = get_user_model()
                notes_query = notes_query.filter(author = User.objects.get(username = username))
                notes_query = notes_query.exclude(personal = "private")
                return Response(notes_query.data, status = 200)


            # Exclude personal notes
            notes_query = notes_query.exclude(personal="personal")

            # Serialize the filtered notes
            serializer = NotesSerializer(notes_query, many=True)
            if serializer:
                return Response(serializer.data, status=status.HTTP_200_OK)

class NotesAPIViewPrivate(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        note_id = request.GET.get("id")
        note = Note.objects.filter(Id = note_id).filter(author = request.user)
        serializer = NotesSerializer(note, many=True)
        if serializer:
            return Response(serializer.data, status = 200)
        else:
            return "404"

    def post(self, request, *args, **kwargs):
        received_json_data = json.loads(request.body)
        personal = received_json_data["personal"]
        text = received_json_data["text"]
        theme = received_json_data["theme"]
        author = request.user
        newNote = Note(author = request.user, text = text, theme = theme, personal = personal)
        newNote.save()
        return Response("created", status = 201)
