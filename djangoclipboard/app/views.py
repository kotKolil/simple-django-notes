from django.template.response import *
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from hashlib import sha256

from .models import *


def index(request):
    section = request.GET.get("section")
    if section == "personal" and not request.user.is_authenticated:
        return redirect("/log_in")
    note_data = Note.objects.all()
    return TemplateResponse(request, "index.html", context={
        "note": note_data,
        "option": section,
        "username": request.user
    }
                            )


def newNote(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return TemplateResponse(request, "editor.html")
        return redirect("/log_in")
    elif request.method == "POST":
        if request.user.is_authenticated:
            note_type = request.POST.get("note-type") if request.POST.get("note-type") is not None else "common"
            theme = request.POST.get("theme")
            text = request.POST.get("text")
            new_note = Note(author=request.user, text=text, theme=theme, personal=note_type)
            new_note.save()
            return redirect("/")
        return redirect("/log_in")


def findView(request):
    if request.method == "POST":
        tag_name = request.POST.get("tag_name")
        note_data = Note.objects.filter(theme__icontains=tag_name)
        return TemplateResponse(request, template="index.html", context={"note": note_data})


def logIn(request):
    if request.method == "GET":
        return TemplateResponse(request, "log_in.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            print("logged in")
            login(request, user)
            return redirect("/")
        return render(request, "log_in.html", {"text": "incorrect username or password"})


def regIn(request):
    if request.method == "GET":
        return TemplateResponse(request, "reg_in.html")
    elif request.method == "POST":

        sha256()

        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        newUser = User.objects.create_user(username=username, password=password, email=email)
        newUser.save()
        return redirect("/")


def viewNote(request):
    if request.method == "GET":
        noteId = request.GET.get("id")
        noteData = Note.objects.get(Id=noteId)
        if noteData and noteData.personal != "personal":
            return render(request, "note.html", context={
                "theme": noteData.theme,
                "text": noteData.text,
                "author": noteData.author.username,
                "noteId": noteData.Id,
            })
        elif noteData and noteData.personal == "personal" and noteData.author == request.user:
            return render(request, "note.html", context={
                "theme": noteData.theme,
                "text": noteData.text,
                "author": noteData.author.username,
                "noteId": noteData.Id,
            })
        return render(request=request, template_name="note.html", context={
            "theme": "HTTP 404. Not Found",
            "author": request.user.username
        })
