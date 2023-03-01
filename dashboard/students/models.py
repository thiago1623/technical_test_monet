from django.db import models
from django.contrib.auth.models import User as AuthUser


class Answer(models.Model):
    text = models.TextField(null=True)
    auth_user = models.ForeignKey(AuthUser, default=None, null=True, on_delete=models.SET_NULL)
    order = models.IntegerField(null=True)  # TODO default=1?
    is_correct = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}, {self.is_correct}'

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
        return f'{self.pk}, {self.text}'

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


class Score(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True)
    percentage = models.FloatField(null=True)   # between 0-100 this is to show on the UI!
    passed = models.BooleanField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id={self.pk}'

    class Meta:
        db_table = 'scores'


class Student(models.Model):
    user = models.ForeignKey(AuthUser, null=True, on_delete=models.CASCADE)
    scores = models.ManyToManyField(Score)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        db_table = 'students'
