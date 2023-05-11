from django.urls import path
from .views import RegisterAPIView, LoginAPIView, RUDAPIView


urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('profile/<int:pk>/', RUDAPIView.as_view()),
]