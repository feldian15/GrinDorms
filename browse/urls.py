from django.urls import path
from . import views

app_name = "browse"
urlpatterns = [
    path('', views.browse, name="browse"),
    path('<str:building_name>/<int:room_number>/', views.room_details, name="room_details")
]