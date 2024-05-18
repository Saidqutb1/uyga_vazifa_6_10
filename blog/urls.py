from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('', register, name='article_list'),
]
