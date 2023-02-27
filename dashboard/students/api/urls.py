from django.urls import re_path
from ..api.views import login_and_register
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    re_path(r'^auth/register/v1$', login_and_register.student_register),
    re_path(r'^auth/register/v2$', login_and_register.RegisterAPIview.as_view()),
    re_path(r'^auth/login$', TokenObtainPairView.as_view()),
    re_path(r'^auth/refresh-token$', TokenRefreshView.as_view()),
]
