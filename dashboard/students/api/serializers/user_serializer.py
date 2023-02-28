from rest_framework import serializers
from django.contrib.auth.models import User as AuthUser
from collections.abc import Iterable
from rest_framework.serializers import ModelSerializer


class ParentModelSerializer(ModelSerializer):
    """
    This is a parent class to some serializers with complex behaviours. Override method process(obj, **kwargs) and add
    additional params in kwargs. Those params should be added in the instantiation.
    Abstracts some common code to complex objects. Before initializing object will run method process.
    """

    def __init__(self, *args, **kwargs):

        if len(args) > 0:
            objs = args[0]
            objs = self.__class__._process(objs, **kwargs)
            super().__init__(objs)  # if we pass kwargs, there will be an error with passing of additional keys
        else:
            super().__init__(**kwargs)

    @staticmethod
    def process(obj, **kwargs):
        return obj

    @classmethod
    def _process(cls, objs, **kwargs):

        if objs is None:
            return None

        if isinstance(objs, cls.Meta.model):  # indicates that it is a django model
            return cls.process(objs, **kwargs)
        elif isinstance(objs, Iterable):
            return [cls.process(obj, **kwargs) for obj in objs]
        else:
            raise NotImplementedError(f'Object should be of class Iterable or {cls.Meta.model}, but found {type(objs)}')


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


class UserSerializer(ParentModelSerializer):
    complete_name = serializers.CharField(max_length=200)

    class Meta:
        model = AuthUser
        fields = ('pk', 'complete_name', 'email', 'username')

    @staticmethod
    def process(user, **kwargs):
        user.complete_name = f'{user.first_name} {user.last_name}'
        return user
