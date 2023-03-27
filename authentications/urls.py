from .views import *
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('resetPassword', ResetPasswordView.as_view(), name='resetPassword'),
    path('setNewPassword', SetNewPasswordView.as_view(), name='setNewPassword'),
    path('usernameValidation',csrf_exempt(UsernameValidationView.as_view()), name="username validation"),
    path('emailValidation',csrf_exempt(EmailValidationView.as_view()), name="email validation"),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate')
]
