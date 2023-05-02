from rest_framework import generics, permissions
from .serializers import CourseSerializer, LessonCreateSerializer, LessonFilesSerializer
from .models import Course, Lesson, LessonFiles
from .permissions import IsOwnerOrReadOnly, IsTeacherOrReadOnly


class CourseListCreateAPIView(generics.ListCreateAPIView):
    #  http://127.0.0.1:8000/course/list_create/
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsTeacherOrReadOnly]


class LessonCreateAPIView(generics.CreateAPIView):
    #  http://127.0.0.1:8000/course/lesson/create/
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer
    permission_classes = [IsOwnerOrReadOnly]


class LessonRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    #  http://127.0.0.1:8000/course/lesson/detail/<int:pk>/
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer
    permission_classes = [IsOwnerOrReadOnly]


class LessonFilesCreateAPIView(generics.CreateAPIView):
    #  http://127.0.0.1:8000/course/lesson_files/create/
    queryset = LessonFiles.objects.all()
    serializer_class = LessonFilesSerializer
    permission_classes = [IsOwnerOrReadOnly]


class LessonFilesRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    #  http://127.0.0.1:8000/course/lesson_files/detail/<int:pk>/
    queryset = LessonFiles.objects.all()
    serializer_class = LessonFilesSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CourseLastThreeListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/blog/list/last_three_courses/
    queryset = Course.objects.all()[:3]
    serializer_class = CourseSerializer