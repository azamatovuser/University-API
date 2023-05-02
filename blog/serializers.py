from rest_framework import serializers
from .models import Post, Body, Comment
from main.serializers import CategorySerializer, TagSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'parent_comment', 'body', 'created_date', 'top_level_comment_id']


class PostListSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'image', 'created_date', 'comments']


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = ['id', 'post', 'body', 'is_script']


class PostDetailSerializer(serializers.ModelSerializer):
    body = BodySerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'image', 'body', 'category', 'tags', 'comments', 'created_date']