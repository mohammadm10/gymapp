from django.urls import path
from .views import AddWeightAPIView

urlpatterns = [
    path('addWeight/', AddWeightAPIView.as_view(), name='addWeight')
]