from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import UpdateView


class MyLoginView(LoginView):
    template_name = "registration/login.html"


class HomeView(View):
    template_name = "registration/home.html"


class RegisterView(UpdateView):
    template_name = "registration/register"