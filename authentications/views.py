from django.shortcuts import render
from django.views import View

# Create your views here.

class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
class ResetPasswordView(View):
    def get(self, request):
        return render(request, 'authentication/resetPassword.html')
class SetNewPasswordView(View):
    def get(self, request):
        return render(request, 'authentication/setNewPassword.html')
