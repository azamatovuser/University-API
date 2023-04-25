from django.urls import path
from .views import CourseListCreateAPIView, LessonCreateAPIView, LessonFilesCreateAPIView, LessonRUDAPIView, LessonFilesRUDAPIView


urlpatterns = [
    path('list_create/', CourseListCreateAPIView.as_view()),
    path('lesson/create/', LessonCreateAPIView.as_view()),
    path('lesson/detail/<int:pk>/', LessonRUDAPIView.as_view()),
    path('lesson_files/create/', LessonFilesCreateAPIView.as_view()),
    path('lesson_files/detail/<int:pk>/', LessonFilesRUDAPIView.as_view()),
]