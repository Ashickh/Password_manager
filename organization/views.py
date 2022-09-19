from django.shortcuts import render

from organization.serializers import UserRegistrationSerializer,UserSerializer
from django.contrib.auth.models import User
from organization.models import AddUserModel
from rest_framework import viewsets
from rest_framework import permissions,authentication

# Create your views here.


class SignupModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    model=User


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = AddUserModel.objects.all()
    model=AddUserModel
    # authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

