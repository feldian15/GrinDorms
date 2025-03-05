from django.urls import path
from . import views

app_name = "browse"
urlpatterns = {
    path("", views.home, name = "home"),
    path("filter=<str:args>/", views.rooms_updated, name = "rooms_updated"),
    path("<str:building_name>/", views.floors, name = "floors"),
    path("<str:building_name>/<int:floor_num>/", views.rooms, name = "rooms"),
    path("<str:building_name>/<int:floor_num>/<int:room_number>/", views.room_details, name = "room_details")
}