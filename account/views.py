import requests.cookies
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Profile
import jwt, datetime


class RegisterAPIView(APIView):
    #  http://127.0.0.1:8000/account/register/
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    #  http://127.0.0.1:8000/account/login/
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = Profile.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {'id': user.id,
                   'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                   'iat': datetime.datetime.utcnow()}
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
    
    
class ProfileAPIView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError :
            raise AuthenticationFailed('Unauthenticated!')
        user = Profile.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
