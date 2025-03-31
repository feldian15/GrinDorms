from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "login"
urlpatterns = [

    path('', views.homepage, name=""),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('user-logout', views.user_logout, name="user-logout"),

    path("activate/<str:uidb64>/<str:token>/", views.activate, name="activate"),

    path('resend-registration', views.resend_registration, name="resend-registration"),

    path('registration-submitted', views.registration_submitted, name="registration-submitted"),


    # Password Reset Links
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password_reset_complete'),

]
