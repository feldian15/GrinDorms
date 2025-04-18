from django.apps import AppConfig

# Reference this sub-app with the name "login"
class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login'
