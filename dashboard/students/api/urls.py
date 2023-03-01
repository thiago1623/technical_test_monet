from django.urls import re_path
from ..api.views import login_and_register, views_for_tests_and_questions
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    re_path(r'^auth/register/v1$', login_and_register.student_register),
    re_path(r'^auth/register/v2$', login_and_register.RegisterAPIview.as_view()),
    re_path(r'^auth/login$', TokenObtainPairView.as_view()),
    re_path(r'^auth/refresh-token$', TokenRefreshView.as_view()),
    re_path(r'^auth/create-test(/(?P<test_id>\d+))?$', views_for_tests_and_questions.create_test_api),
    re_path(r'^auth/save-answer$', views_for_tests_and_questions.save_user_answer_selected),
    re_path(r'^auth/student/answers$', views_for_tests_and_questions.view_student_answers, name='view_student_answers'),
]
