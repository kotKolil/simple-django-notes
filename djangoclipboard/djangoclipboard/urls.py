"""
URL configuration for django clipboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. Home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import *
from django.conf.urls.static import static
from django.urls import *
from app import *
from app.API import views as APIViews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

apiViews = [
    path("api/Note/", APIViews.NotesAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("", views.index),
                  path("newNote/", views.newNote),
                  path("log_in/", views.logIn),
                  path("note/", views.viewNote),
                  path("reg/", views.regIn),
                  path("find/", views.findView),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + apiViews
