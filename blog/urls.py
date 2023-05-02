from django.urls import path
from .views import PostListAPIView, CategoryListAPIView, TagListAPIView, PostDetailAPIView
from course.views import CourseLastThreeListAPIView


urlpatterns = [
    path('list/', PostListAPIView.as_view()),
    path('list/last_three_courses/', CourseLastThreeListAPIView.as_view()),
    path('list/category/', CategoryListAPIView.as_view()),
    path('list/tags/', TagListAPIView.as_view()),
    path('detail/<int:pk>/', PostDetailAPIView.as_view()),
]