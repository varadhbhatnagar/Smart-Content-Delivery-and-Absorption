from django.contrib.auth.models import User
from django import forms
from .models import *

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['First_Name', 'Last_Name', 'Role']


class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PartProfileFormStudent(forms.Form):
        standard = forms.IntegerField()
        section = forms.CharField(max_length=2)


class PartProfileForm(forms.Form):
    subject = forms.CharField(max_length=50, required = False)
    standard = forms.IntegerField()
    section = forms.CharField(max_length=2)

class FileForm(forms.Form):
    file = forms.FileField()