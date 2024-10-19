from django.urls import path, include
from .views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
