from django.urls import path
from . import views

urlpatterns = [
    path('sign-out', views.sign_out, name='sign_out'),
    path('receiver', views.auth_receiver, name='receiver'),
]