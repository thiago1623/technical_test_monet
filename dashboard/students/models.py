from django.db import models
from django.contrib.auth.models import User as AuthUser


class Student(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}, {self.name}'

    class Meta:
        db_table = 'students'


class Answer(models.Model):
    text = models.TextField(null=True)
    auth_user = models.ForeignKey(AuthUser, default=None, null=True, on_delete=models.SET_NULL)
    order = models.IntegerField(null=True)  # TODO default=1?
    is_correct = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}, {self.name}'

    class Meta:
        db_table = 'answers'
        ordering = ['order']


class Question(models.Model):
    text = models.TextField(null=True)
    auth_user = models.ForeignKey(AuthUser, null=True, default=None, on_delete=models.SET_NULL)
    answers = models.ManyToManyField(Answer)
    correct_answers = models.ManyToManyField(Answer, related_name='correct_answers')
    order = models.IntegerField(default=1)
    avg_score = models.FloatField(default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}, {self.text[:15]}'

    class Meta:
        db_table = 'questions'
        ordering = ['order']


class Test(models.Model):
    name = models.CharField(max_length=200, null=True)
    auth_user = models.ForeignKey(AuthUser, null=True, default=None, on_delete=models.SET_NULL)
    questions = models.ManyToManyField(Question)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}, {self.name}'

    class Meta:
        db_table = 'tests'
