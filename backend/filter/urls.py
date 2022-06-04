from django.urls import path

from .views import *

urlpatterns = [
    path('data/', dataView),
    path('recommendFZ/<str:query>/', recommendFZ.as_view()),
    path('recommendUser/<str:query>/', recommendUser.as_view()),
]
