from django.urls import path, include

from Auth import views

app_name = 'Auth'

urlpatterns = [
    path('profile/<int:pk>', views.HomeView.as_view(), name='profile'),

    path('signin', views.Signin.as_view(), name='signin'),

    path('signup', views.Signup.as_view(), name='signup'),

    path('logout', views.MyLogoutView.as_view(), name='logout')
]