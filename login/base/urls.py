from django.urls import path, include
from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
]