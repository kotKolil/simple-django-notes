from django.test import TestCase
from django.test import Client
from djangoclipboard.models import Note

# Create your tests here.
class NoteTestCase(TestCase):


    def setUp(self):
        self.User.objects.create_user(email='test@example.com', password='securepassword')
        Note.objects.create(personal = "common", author = sample_user, text  = "lorum ipsum dolor sit ammet", theme = "#sample")
        Note.objects.create(personal = "private", author = sample_user, text  = "lorum ipsum dolor sit ammet", theme = "#sample")

    def getUser(self):
        c = Client()
        Note = Note.objects.get(text = "lorum ipsum dolor sit ammet")
        response = c.get(f"api/Note/?id={Note.Id}")
        self.assertEqual(response.json()["text"], "lorum ipsum dolor sit ammet")