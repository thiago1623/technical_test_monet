from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User as AuthUser

from students.models import Student


def get_user_from_serializer(serializer):
    try:
        return AuthUser.objects.get(pk=serializer.get('pk')), None
    except ObjectDoesNotExist:
        return None, {'error': 'user not found'}


def create_student(user):
    try:
        return Student.objects.get(pk=user.pk), None
    except ObjectDoesNotExist:
        Student.objects.create(user=user)
