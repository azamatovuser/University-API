from rest_framework import serializers
from course.models import SoldCourse
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'password']