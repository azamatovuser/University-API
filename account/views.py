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

        payload = {'id': user.id,
                   'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                   'iat': datetime.datetime.utcnow()}
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        return Response({
            'jwt': token
        })