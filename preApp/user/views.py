from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout


from .forms import RegisterForm, LoginForm


# Create your views here.


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
