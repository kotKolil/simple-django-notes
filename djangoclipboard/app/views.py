from django.template.response import TemplateResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from hashlib import sha256

from .models import *

# Create your views here.
def index(request):
    note_data = Note.objects.all()
    return TemplateResponse(request, "index.html", context = {"note":note_data})

def newNote(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return TemplateResponse(request, "editor.html")
        return redirect("/log_in")
    elif request.method == "POST":
        if request.user.is_authenticated:
            theme = request.POST.get("theme")
            text = request.POST.get("text")
            newNote = Note(author = request.user, text = text, theme = theme)
            newNote.save()
            return redirect("/")
        return redirect("/log_in")


def logIn(request):
    if request.method == "GET":
        return TemplateResponse(request, "log_in.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            print("logged in")
            login(request, user)
            return redirect("/")
        return render("log_in.html", {"text": "incorrect username or password"})


def regIn(request):
    if request.method == "GET":
        return TemplateResponse(request, "reg_in.html")
    elif request.method == "POST":

        hasher = sha256()

        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        newUser = User.objects.create_user(username = username, password = password, email = email)
        newUser.save()
        return redirect("/")

def viewNote(request):
    if request.method == "GET":
        noteId = request.GET.get("id")
        noteData = Note.objects.get(Id = noteId)
        return render(request, "note.html", context = {
            "theme": noteData.theme,
            "text": noteData.text,
            "author": noteData.author.username
        })