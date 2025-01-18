from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    return TemplateResponse(request, "editor.html")