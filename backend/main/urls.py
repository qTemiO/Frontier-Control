from django.urls import path

from .views import ComplexView

urlpatterns = [
    path('complex/<str:query>/', ComplexView.as_view())
]
