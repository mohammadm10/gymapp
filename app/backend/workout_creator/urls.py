from django.urls import path
from .views import APIWorkoutGenAPIView

urlpatterns = [
    path('workout_creator/', APIWorkoutGenAPIView.as_view(), name='workout_creator')
]
