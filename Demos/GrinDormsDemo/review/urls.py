from django.urls import path
from . import views

app_name = "review"
urlpatterns = [
    path("", views.review, name = "review"),
    path("add/<str:building_name>/<int:room_number>/", views.add, name="add"),
    path("myreviews/", views.my_reviews, name="my_reviews"),
    path("review_added/", views.review_added, name="review_added"),
    path("remove/", views.remove, name="remove"),
    path("review_removed/", views.review_removed, name="review_removed")
]