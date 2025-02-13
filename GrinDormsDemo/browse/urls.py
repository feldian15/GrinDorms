from django.urls import path
from . import views

app_name = "browse"
urlpatterns = {
    path("", views.home, name = "home"),
    path("<str:building_name>/", views.floors, name = "floors"),
    path("<str:building_name>/<int:floor_number>/", views.rooms, name = "rooms"),
    path("<str:building_name>/<int:floor_number>/<int:room_number>/", views.room_details, name = "room_details")
}