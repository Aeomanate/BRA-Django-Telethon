from django.urls import path, include

from Auth import views

app_name = 'auth'

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),

    path('', views.MyLoginView.as_view(), name='login'),

    path('reg', views.RegisterView.as_view(), name='register')
]