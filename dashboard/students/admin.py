from django import forms
from django.forms import Media
from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Student, Test, Question, Answer, Score


class ScoreStudent(models.Model):
    score = models.ForeignKey(Score, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class ScoreInline(admin.TabularInline):
    model = ScoreStudent
    extra = 1
    verbose_name_plural = 'Scores'


class QuestionInline(admin.TabularInline):
    model = Question.answers.through
    extra = 0
    verbose_name_plural = 'Answers'


class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


class StudentAdmin(admin.ModelAdmin):
    inlines = [ScoreInline]


admin.site.register(Answer)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Score)
admin.site.register(Student, StudentAdmin)
