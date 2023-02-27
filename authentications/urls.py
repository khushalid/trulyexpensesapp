from .views import *
from django.urls import path

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('resetPassword', ResetPasswordView.as_view(), name='resetPassword'),
    path('setNewPassword', SetNewPasswordView.as_view(), name='setNewPassword'),
]
