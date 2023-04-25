from rest_framework import serializers
from .models import Course, Lesson, LessonFiles, SoldCourse
from main.serializers import CategorySerializer, TagSerializer


class LessonFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonFiles
        fields = ['id', 'lesson', 'file', 'is_main']


class LessonSerializer(serializers.ModelSerializer):
    lesson_files = LessonFilesSerializer(read_only=True, many=True)

    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'body', 'lesson_files']


class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'body']


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ['id', 'author', 'title', 'difficulty', 'body', 'cover', 'detail_cover', 'lessons', 'category', 'tags',
                  'price', 'is_free', 'discount_price']
