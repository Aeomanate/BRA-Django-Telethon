from django.urls import path, include

from Auth import views

app_name = 'Auth'

urlpatterns = [
    path('profile', views.ProfileView.as_view(), name='profile'),

    path('login', views.Login.as_view(), name='login'),

    path('register', views.Register.as_view(), name='register'),

    path('logout', views.MyLogoutView.as_view(), name='logout')
]