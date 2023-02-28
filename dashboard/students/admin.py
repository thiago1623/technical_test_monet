from django import forms
from django.forms import Media
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Student, Test, Question, Answer


class AnswerInlineForm(forms.ModelForm):
    class Meta:
        model = Question.answers.through
        fields = '__all__'
        widgets = {
            'answer': forms.CheckboxSelectMultiple(),
        }


class AnswerInline(admin.TabularInline):
    model = Question.answers.through
    form = AnswerInlineForm
    extra = 0
    verbose_name_plural = 'answers'


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline, ]
    exclude = ('answers',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "correct_answers":
            kwargs["queryset"] = Answer.objects.filter(question=request.resolver_match.kwargs['object_id'])
        return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Student)
admin.site.register(Test)
admin.site.register(Answer)
