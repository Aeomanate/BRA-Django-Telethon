from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from django.conf import settings


class Signin(LoginView):
    template_name = "registration/signin.html"
    next_page = "/"

    def get_success_url(self):
        # Redirect to the CustomerStats stats page for the user's client
        from CustomerStats.models import Client
        user = self.request.user
        client = Client.objects.filter(user=user).first()
        if client:
            return reverse('stats:stats', kwargs={'client_id': client.id})
        # Fallback if no client is linked to this user
        return reverse('index')


class HomeView(View):
    template_name = "registration/profile.html"


class Signup(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, form.instance)
        # Ensure the new user has an associated Client record
        try:
            from CustomerStats.models import Client
            Client.objects.get_or_create(user=form.instance, defaults={'name': form.instance.username})
        except Exception:
            # Avoid breaking signup on any unexpected error
            pass
        return response

    def get_success_url(self):
        return reverse_lazy('CustomerStats:index')


class MyLogoutView(LogoutView):
    template_name = "registration/logout.html"
    next_page = "Auth:signin"