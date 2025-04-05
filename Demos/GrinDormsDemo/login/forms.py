from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:

        model = User
        fields = ["username", "email", "password1", "password2"]
    
    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("An account with this email already exists.")
        
        if not email.endswith('@grinnell.edu'):
            raise ValidationError("Please use your Grinnell College email address.")
        return email


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



class ResendRegEmailForm(forms.Form):
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        return email
        





