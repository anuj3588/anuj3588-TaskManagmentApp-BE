from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from Task.Api.v1.user_authentication.views import RegisterUserAPIView, GenerateAccessTokenView

urlpatterns = [
    path('register', RegisterUserAPIView.as_view()),
    path('token', GenerateAccessTokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
