from django.urls import path
from . import views

app_name = "review"
urlpatterns = [
    path("", views.review, name = "review"),
    path("<str:building_name>/<int:room_number>/", views.upload, name="upload"),
    path("myreviews/", views.my_reviews, name="my_reviews"),
    path("review_added", views.review_added, name="review_added")
]