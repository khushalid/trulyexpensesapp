from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages 
from django.core.mail import EmailMessage
from validate_email import validate_email
import json

from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import account_activation_token
from django.contrib import auth

from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator


# Create your views here.

class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    def post(self, request):

        # GET USER DATA
        # VALIDATE
        # CREATE USER ACCOUNT

        # delete a user ->
        # User.objects.filter(id=i).delete()

        # get all users ->
        print("users: ", User.objects.values())

        # delete all users at once
        print("users: ", User.objects.values())
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
 
        context = {
            'field_values': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, "Password too short!")
                    return render(request, 'authentication/register.html', context)
                
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()

                # getting the domain we are on
                domain = get_current_site(request).domain
                # encode user id
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                # getting token from token generator
                # relative url to verification
                link = reverse('activate', kwargs = {'uidb64': uidb64, 'token': account_activation_token.make_token(user)})

                activate_url = 'http://'+domain+link
                email_subject = 'Activate Your Account'
                email_body = 'Hi ' + user.username + "\n\nPlease use this link to verify your account using the following link\n" + activate_url
                email = EmailMessage(
                    email_subject,
                    email_body,
                    'khushalidaga87805@gmail.com',
                    [email]
                )
                email.send(fail_silently=False)
                messages.success(request, "User created successfully")
                return render(request, 'authentication/login.html')
            
        return render(request, 'authentication/login.html')

class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            # decoding the user id 
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                print("acount activated already, token")
                return redirect('login' + '?message=' + 'User already activated')
            # if user was activated before
            if user.is_active:
                print("acount activated already, is_active=true")
                return redirect('login')
            
            # else set is_active true and save user
            user.is_active=True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')
            
        except Exception as identifier:
            pass

    
class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'can only use alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'sorry username is in use, choose another one'}, status=409)
        return JsonResponse({'username_valid': True})
    
class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'sorry email is in use, choose another one'}, status=409)
        return JsonResponse({'email_valid': True})
    
class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    @method_decorator(csrf_protect)
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome ' + user.username + '. You are now logged in!')
                    return redirect('costing')
                messages.error(request, 'Account is not active, please check your email')
                return render(request, 'authentication/login.html')
            messages.error(request, 'Invalid Credentials, try again!')
            return render(request, 'authentication/login.html')
        messages.error('Please fill all fields')
        return render(request, request, 'authentication/login.html')

class ResetPasswordView(View):
    def get(self, request):
        return render(request, 'authentication/resetPassword.html')
class SetNewPasswordView(View):
    def get(self, request):
        return render(request, 'authentication/setNewPassword.html')
    
class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out!')
        return redirect('login')
