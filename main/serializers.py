from rest_framework import serializers
from .models import Contact, Subscribe, FAQ, Answer, Category, Tag


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'body', 'created_date']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['id', 'email']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'answer']


class FAQSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(read_only=True, many=True)
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answers']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']