from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Note
from django.contrib.auth import get_user_model
from .serializers import *
from rest_framework.permissions import *
import json

class NotesAPIViewCommon(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        note_id = request.GET.get("id")
        note = Note.objects.filter(Id = note_id).first()
        if note and note.personal != "personal":
            serialized_data = NotesSerializer(note)
            if serialized_data:
                return Response(serialized_data.data)
        elif note and note.personal == "personal" and note.author == request.user.username:
            serialized_data = NotesSerializer(note)
            if serialized_data:
                return Response(serialized_data.data)
        return Response("404", status=404)
    
    def post(self, request):
        requestJson = json.loads(request.body)
        personal = requestJson["personal"]
        text = request["text"]
        theme = request["theme"]
        
        newNote = Note(personal = personal, author = request.user, text  = text, theme = theme)
        newNote.save()
        return Response("200", status = 200)

    def delete(self, request):
        note_id = request.GET.get("id")
        note = Note.objects.filter(Id = note_id)
        if note.author == request.user and note:
            note.delete()
            return Response("200", status=200)
        return Response("404", status = 404)