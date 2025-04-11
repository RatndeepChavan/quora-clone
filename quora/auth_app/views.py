"""auth_app's view file to write business logic."""

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


def home(request):
    """home screen view.

    Args:
        request (WSGIRequest): request object received from client

    Returns:
        HTMLTemplate: HTML template for client with desire output
    """
    print(type(request))
    return render(request, "base.html")


class Signup(CreateView):
    """Class view to register user

    Args:
        CreateView (GenericView): generic view that simplifies create operation.

    Returns:
        HTMLTemplate: HTML template for client with desire output
    """

    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        valid = super().form_valid(form)
        form_data = form.cleaned_data
        username = form_data.get("username")
        password = form.cleaned_data.get("password1")
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid
