"""
Django settings for grindormsdemo project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

# Email Backend Setup
from pathlib import Path
from dotenv import load_dotenv
import os
import environ

load_dotenv()

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = f'{os.getenv("SECRET_KEY")}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = f'{os.getenv("DEBUG")}'

# RECLAIM HAS THE FOLLOWING OPEN PORTS:
# 80, 8080, 8686, 8443, 4848, 4949, 7979
# USING THE PUBLIC IP ALLOWS FOR ALL PORTS TO BE USED.
PORT=os.environ.get('PORT', 8080)

ALLOWED_HOSTS = ['csc-234.us.reclaim.cloud', '135.148.74.19', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'login.apps.LoginConfig',
    'review.apps.ReviewConfig',
    'home.apps.HomeConfig',
    'browse.apps.BrowseConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'grindormsdemo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'grindormsdemo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if(f'{os.getenv("ENVTYPE", "error")}' == "DEVELOPER"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'grindorms', 
            'USER': f'{os.getenv("PG_USER")}',
            'PASSWORD': f'{os.getenv("PG_PWD")}',
            'HOST': f'{os.getenv("PG_HOST")}', 
            'PORT': f'{os.getenv("PG_PORT")}',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'home', 'static', ),
    os.path.join(BASE_DIR, 'browse', 'static', )
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Email Backend Setup
mail = os.environ.get("MAIL")
mail_pass = os.environ.get("PASSWORD")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = mail
EMAIL_HOST_PASSWORD = mail_pass
DEFAULT_FROM_EMAIL = mail

LOGIN_REDIRECT_URL = "/"