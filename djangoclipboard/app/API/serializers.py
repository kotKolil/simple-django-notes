from rest_framework import serializers

from app.models import Note


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["Id", "personal", "author", "text", "theme"]
