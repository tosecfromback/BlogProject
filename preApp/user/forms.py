from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms

User = get_user_model()

# class RegisterForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = [ 'id']

class LoginForm(AuthenticationForm):

    class Meta:
        medel = User
        fields = [ 'id', 'password']
        

class RegisterForm(forms.ModelFrom):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    passwordck = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['id', 'nickname', 'email', 'password']

    def clean_password2(self):
        cd = self.cleand_data
        if cd['password'] != cd ['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']