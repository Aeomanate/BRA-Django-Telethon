from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
class MyLoginView(LoginView):
    template_name = 'registration/login.html'

