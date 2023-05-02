from rest_framework import generics
from .models import Post, Body, Comment
from .serializers import PostListSerializer, PostDetailSerializer
from main.models import Category, Tag
from main.serializers import CategorySerializer, TagSerializer


class PostListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/blog/list/
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class CategoryListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/blog/list/category/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/blog/list/tags/
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    #  http://127.0.0.1:8000/blog/detail/<int:post_id>/
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer