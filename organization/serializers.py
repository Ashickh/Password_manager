from rest_framework import serializers
from django.contrib.auth.models import User
from organization.models import AddUserModel

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "username",
            "email",
            "password"
        ]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddUserModel
        fields="__all__"