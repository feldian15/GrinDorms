from django.urls import path
from . import views

# Ensure this matches the name of the folder it is in
app_name = "home"

urlpatterns = [
    path('', views.homepage, name="homepage")
]
