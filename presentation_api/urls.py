from django.urls import path
from .views import PresentationView

urlpatterns = [
    path('presentation/', PresentationView.as_view(), name='presentation'),
]
