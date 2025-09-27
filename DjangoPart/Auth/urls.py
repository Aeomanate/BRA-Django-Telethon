from django.urls import path

from DjangoPart.Auth.views import MyLoginView

app_name = 'Auth'
urlpatterns = [
    path('', MyLoginView.as_view(), name='login'),
]