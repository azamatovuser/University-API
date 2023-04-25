from rest_framework import generics, permissions
from .models import Contact, Subscribe, FAQ, Answer, Category, Tag
from .serializers import ContactSerializer, SubscribeSerializer, FAQSerializer, AnswerSerializer, CategorySerializer, TagSerializer


class ContactListCreateAPIView(generics.ListCreateAPIView):
    #  http://127.0.0.1:8000/main/contact/
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class SubscribeListCreateAPIView(generics.ListCreateAPIView):
    #  http://127.0.0.1:8000/main/subscribe/
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


class FAQListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/main/faq/
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class AnswerCreateAPIView(generics.CreateAPIView):
    #  http://127.0.0.1:8000/main/answer_create/
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    #  http://127.0.0.1:8000/main/category/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TagListCreateAPIView(generics.ListCreateAPIView):
    #  http://127.0.0.1:8000/main/tag/
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]