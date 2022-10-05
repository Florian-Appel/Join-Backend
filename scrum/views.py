from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from scrum.serializers import RegisterSerializer, TaskSerializer, UserSerializer
from .models import Task

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet): 
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]


class UserDetailAPI(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class RegisterUserAPIView(generics.CreateAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
