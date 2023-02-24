from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.authtoken import views

urlpatterns = [
    path('', hello_world),
    path('register', RegisterUser.as_view()),
    path('login', CustomAuthToken.as_view()),
    path('users', UserView.as_view())
]