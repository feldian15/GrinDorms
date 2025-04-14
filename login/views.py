### *****************
### views.py
### Author: Ella Berman
### Defines functions that get called from the login subapp, determines what information gets collected from users,
### and tells the frontend what html to render.
### *****************

from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, ResendRegEmailForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,  urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import account_activation_token
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# renders homepage 
def homepage(request):
    messages_to_display = messages.get_messages(request)
    return render(request, 'login/index.html', {"messages": messages_to_display})

# renders the register page, an provides a form for the user to provide login info to create their account
def register(request):
    form = CreateUserForm()
    # define that this info is being sent to the backend
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        #check that the form has all necessary information is filled
        if form.is_valid():
            user = form.save(commit = False)
            user.is_active = False
            user.save()

            # generates and sends an email with a semi-unique link to the user so that they can activate their account.
            current_site = get_current_site(request)
            mail_subject = "Activate your GrinDorms account"
            message = render_to_string("login/account_activation_email.html",{ 
                "user":user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": account_activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get("email")
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return redirect("login:registration-submitted")
    return render(request, 'login/register.html', {"registerform":form})

# renders the login page and grab its info
def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # grab data from the form and authenticates it
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            # supposing the user is real, take them to the homepage, otherwise show an error message.
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect("home:homepage")
                else:
                    messages.error(request, "Your account is not activated. Please check your email to activate your account.")
                    return redirect("login:my-login")
    
    # provide the form to the frontend and render the html
    # TODO be consistent with if we are putting objects in render functions
    # TODO go fuck myself
    context = {'loginform':form}
    return render(request, 'login/my-login.html', context=context)

# this is no longers needed.
# TODO delete this, does not seem to be referenced anywhere
def dashboard(request):
    return render(request, 'login/dashboard.html')

# logs out and redirects the user to the login page upon logout
def user_logout(request):
    auth.logout(request)
    return redirect("login:")

# when a user clicks their activiation link, go here. and let the activate their account.
def activate(request, uidb64, token):
    User = get_user_model()

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        login(request, user)

        # since this is a static url the reverse should be redundant.
        return redirect(reverse("login:my-login"))
    else:
        messages.error(request, "Activation link is invalid or expired.")
        return redirect("login:")

# this is self explainitory, although there is potential for repeated code from the register function.
# TODO see if we can refactor this to be more DRY
def resend_registration(request):
    form = ResendRegEmailForm()

    if request.method == "POST":
        form = ResendRegEmailForm(request.POST)

        if form.is_valid():
            email = request.POST.get('email')

            try:
                user = User.objects.get(email=email)

                if user is not None:
                    if user.is_active:
                        raise ValidationError("Your account is already active. Please sign in.")
                    else:
                        current_site = get_current_site(request)
                        mail_subject = "Activate your GrinDorms account"
                        message = render_to_string("login/account_activation_email.html",{ 
                            "user":user,
                            "domain": current_site.domain,
                            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                            "token": account_activation_token.make_token(user)
                        })
                        to_email = form.cleaned_data.get("email")
                        email = EmailMessage(
                            mail_subject, message, to=[to_email]
                        )
                        email.send()
                        messages.success(request, "Please check your email to complete the registration process. It might be in your spam folder.")
                        # TODO reslove inconsistency with redirecting vs rendering registartion_submitted from this to
                            # TODO normal register function
                        return render(request, "login/registration_submitted.html")

            except User.DoesNotExist:
                raise ValidationError("No account with this email was found.")

    return render(request, "login/resend_registration.html", {"resendregistration":form})

# this is the page that renders when the user either clicks the log in button on the login page
def registration_submitted(request):
    return render(request, "login/registration_submitted.html")