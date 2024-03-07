from django import forms
from django.db import models
from django.forms import ModelForm
from n_sequential_passwords.models import User

class PinForm(ModelForm):
    pin = forms.IntegerField(max_value = 5)

    class Meta:
        model = User
        fields = ("username", "pin")

class PasswordForm(ModelForm):
    password = forms.CharField(max_length=16)

    class Meta:
        model = User
        fields = ("username", "password")

class PasswordForm1(forms.Form):
    password = forms.CharField(label='Enter your password')

class PinForm1(forms.Form):
    pin = forms.IntegerField(label='Enter your pin')
