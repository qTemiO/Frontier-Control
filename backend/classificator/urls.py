from django.urls import path

from .views import *

urlpatterns = [
    path('classificatorUser/<str:query>/', ClassificatorView.as_view()),
]
