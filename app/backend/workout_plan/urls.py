from django.urls import path
from .views import WorkoutPlanAPIView

urlpatterns = [
    path('workout_plan/', WorkoutPlanAPIView.as_view(), name='workoutPlan')
]
