from django.urls import path,include
from .views import KalaViewser

urlpatterns = [
    path("",KalaViewser.as_view()),
]
