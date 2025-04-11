from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


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
