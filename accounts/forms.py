from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

#import django models
class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    employee_number = forms.CharField(max_length=4, label="Employee Number")
    class Meta:
        model =  User
        fields = ['username','employee_number', 'email', 'password1', 'password2']