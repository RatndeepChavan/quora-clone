from django.urls import include, path

from . import views

urlpatterns = [
    path("signup/", views.Signup.as_view(), name="signup"),
    path("", include("django.contrib.auth.urls")),
]
