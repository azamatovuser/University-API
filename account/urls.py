from django.urls import path
from .views import RegisterAPIView, LoginAPIView, ProfileAPIView


urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),
]