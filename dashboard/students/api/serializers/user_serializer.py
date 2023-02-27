from rest_framework import serializers
from django.contrib.auth.models import User as AuthUser


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=200, write_only=True)

    class Meta:
        model = AuthUser
        fields = ('pk', 'first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, user):
        email = user.get('email', None)
        user_name = user.get('username', None)
        if AuthUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'email already exists'})
        if AuthUser.objects.filter(username=user_name).exists():
            raise serializers.ValidationError({'username': 'name already exists'})
        return user

    def create(self, validated_data):
        return AuthUser.objects.create_user(**validated_data)

