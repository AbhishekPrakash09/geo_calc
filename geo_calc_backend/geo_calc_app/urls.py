from django.urls import path
from .views import UserCreateView, CustomTokenObtainPairView

from rest_framework_simplejwt.views import (
   
    TokenRefreshView,
)

urlpatterns = [
    path('register', UserCreateView.as_view(), name='user_register'),
    path('token',  CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT obtain token
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
