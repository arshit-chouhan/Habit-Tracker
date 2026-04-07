
from django.urls import path
from .api_views import HabitListAPI

urlpatterns = [
    path('habits/', HabitListAPI.as_view())
]
