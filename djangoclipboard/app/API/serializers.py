import sys

sys.path.append("...")
from app.models import Note
from rest_framework import serializers


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["Id", "personal", "author", "text", "theme"]
