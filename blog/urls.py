from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.all_blogs, name='all_blogs')
]
