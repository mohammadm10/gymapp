from django.urls import path
from .views import CalculateRepAPIView

urlpatterns = [
    path('rep_max_calculator/', CalculateRepAPIView.as_view(), name='calculateRep')
]
