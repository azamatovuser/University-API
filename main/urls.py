from django.urls import path
from .views import ContactListCreateAPIView, SubscribeListCreateAPIView, FAQListAPIView, AnswerCreateAPIView, CategoryListCreateAPIView, TagListCreateAPIView

urlpatterns = [
    path('contact/', ContactListCreateAPIView.as_view()),
    path('subscribe/', SubscribeListCreateAPIView.as_view()),
    path('faq/', FAQListAPIView.as_view()),
    path('answer_create/', AnswerCreateAPIView.as_view()),
    path('category/', CategoryListCreateAPIView.as_view()),
    path('tag/', TagListCreateAPIView.as_view()),
]