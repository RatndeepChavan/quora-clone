"""Url path declaration for question_app's views."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("create/", views.QuestionCreateView.as_view(), name="create"),
    path("<int:pk>", views.QuestionDetailView.as_view(), name="detail"),
    path("like/<int:question_pk>/<int:answer_pk>/", views.like, name="like"),
]
