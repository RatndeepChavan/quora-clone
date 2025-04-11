"""Url path declaration for auth_app's views."""

from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.Signup.as_view(), name="signup"),
    path("", include("django.contrib.auth.urls")),
]
