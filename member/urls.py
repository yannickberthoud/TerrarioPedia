from django.urls import path
from .views import ChangePasswordView, profile

urlpatterns = [
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('', profile, name='profile'),
]