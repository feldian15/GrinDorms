### *****************
### forms.py
### Author: Ella Berman
### Defines forms enabling users to enter information and complete tasks for the 
### account creation and verification process. Referenced in views.py. 
### *****************

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

# Form used in the registration page to create a new user. 
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # Create an instance of a user given information in the form
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    def clean_email(self):
        email = self.cleaned_data.get("email").strip().lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("An account with this email already exists.")
        
        if not email.endswith('@grinnell.edu'):
            raise ValidationError("Please use your Grinnell College email address.")
        return email

# Form used to sign in an existing, authenticated user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# Form enabling users to enter their email. Used to resend the verification link.
class ResendRegEmailForm(forms.Form):
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get("email").strip().lower()
        return email