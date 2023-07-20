from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm


from .forms import RegisterForm, LoginForm


# Create your views here.


class register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_neser' : new_user})
        user_form = RegisterForm()

    return render(request, 'registraion/register.html')

class Registration(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class Login(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class Logout(View):
    def get(self, request):
        pass
    def post(self, request):
        pass
