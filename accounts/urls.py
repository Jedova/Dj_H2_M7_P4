from django.urls import path
from .views import register, profile, profile_edit

app_name = "accounts"

urlpatterns = [
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("profile/editar/", profile_edit, name="profile_edit"),
]
