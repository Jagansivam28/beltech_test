from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('getall/',GetAll.as_view()),
    path("search/",Search.as_view()),
    path("distance/",Distance.as_view()),
]
