from django import forms
from user.models import User
from django.contrib.auth.models import User as usr

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

class SignUpForm(forms.ModelForm):
    class Meta:
        model=usr
        fields=['username','password','email','last_name','first_name']
