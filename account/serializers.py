from rest_framework import serializers
from course.models import SoldCourse
from .models import Profile
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=60, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=60, write_only=True)

    class Meta:
        model = Profile
        fields = ['username', 'role', 'password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError({'success': False, 'message': "Password didn't match, Please try again!"})
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        return Profile.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(max_length=60, write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, obj):  # get_{field_name}
        username = obj.get('username')
        tokens = Profile.objects.get(username=username).tokens
        return tokens

    class Meta:
        model = Profile
        fields = ('username', 'password', 'tokens')

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed({
                'message': "Username or Password wrong, Please try again!"
            })
        if not user.is_active:
            raise AuthenticationFailed({
                'message': 'Account disabled'
            })
        return attrs


class MyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'image', 'first_name', 'last_name', 'role', 'created_date')


class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'first_name', 'last_name', 'role', 'get_role_display')
        extra_kwargs = {
            'role': {'read_only': True}
        }