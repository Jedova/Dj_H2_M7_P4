"""
URL configuration for h2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from inmuebles.views import solo_lectura_inmuebles  # <-- importa la vista protegida

def home(request):
    return HttpResponse("<h1>Bienvenido</h1><p><a href='/admin/'>Admin</a> | <a href='/accounts/logout/'>Cerrar sesión</a></p>")

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),

    path("accounts/", include("django.contrib.auth.urls")),

    path("accounts/", include("accounts.urls")),

    path("inmuebles/solo-lectura/", solo_lectura_inmuebles, name="inmuebles_solo_lectura"),
]
