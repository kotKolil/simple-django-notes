from django.template.response import TemplateResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return TemplateResponse(request, "index.html")

def newNote(request):
    if request.user.is_authenticated:
        return TemplateResponse(request, "editor.html")
    return redirect("/log_in")

def logIn(request):
    if request.method == "GET":
        return TemplateResponse(request, "log_in.html")
    username = request.post.get("username")
    password = request.post.get("password")
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return redirect("/")
    return render("log_in.html", {"text": "incorrect username or password"})