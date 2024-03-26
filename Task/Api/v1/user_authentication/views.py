from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from Task.Api.v1.user_authentication.serializer import RegisterSerializer, GenerateAccessTokenObtainPairSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class GenerateAccessTokenView(TokenObtainPairView):
    serializer_class = GenerateAccessTokenObtainPairSerializer
