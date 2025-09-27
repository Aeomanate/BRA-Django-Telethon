from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login

from django.apps import apps

def get_client_model():
    # Use the app label (as defined by AppConfig.label, commonly the package name)
    return apps.get_model('CustomerStats', 'Client')


# Create your views here.
class MyLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        # Redirect to the user's profile after successful sign-in
        return reverse('Auth:profile')


class RegisterView(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, form.instance)
        # Ensure the new user has an associated Client record

        get_client_model().objects.get_or_create(user=form.instance, defaults={'name': form.instance.username})
        return response

    def get_success_url(self):
        # After registration, redirect to profile page using the logged-in user from the request context
        return reverse('Auth:profile')

class ProfileView(View):
    template_name = "CustomerStatsTW/profile.html"

    def get(self, request):
        # Provide the logged-in user and their Client (if any) to the template context
        user = request.user
        client = None
        if user.is_authenticated:
            client = get_client_model().objects.filter(user=user).first()

        context = {
            'user': user,
            'client': client,
        }
        return render(request, self.template_name, context)
