from django.urls import path
from .views import SignUpAPIView, VerifyView

urlpatterns = [
    path('signUp/', SignUpAPIView.as_view(), name='signup'),
    path('verify/', VerifyView.as_view(), name='verify'),
]