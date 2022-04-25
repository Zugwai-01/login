from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutuser, name="logout"),
    path("register/", views.registerUser, name="register"),
    path("", views.Home, name="home"),
]
