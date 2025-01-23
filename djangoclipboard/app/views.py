from django.template.response import TemplateResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

from .models import *

# Create your views here.
def index(request):
    note_data = Note.objects.all()
    return TemplateResponse(request, "index.html", context = {"note":note_data})

def newNote(request):
    if request.user.is_authenticated:
        return TemplateResponse(request, "editor.html")
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