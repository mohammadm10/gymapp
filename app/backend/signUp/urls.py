from django.urls import path
from .views import SignUpAPIView

urlpatterns = [
    path('signUp/', SignUpAPIView.as_view(), name='signup'),
]