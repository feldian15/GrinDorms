from django.urls import path
from . import views

app_name = "review"
urlpatterns = [
    path('', views.review, name="review"),
    path('my_reviews/', views.my_reviews, name="my_reviews"),
    path('add_success/', views.add_success, name="add_success"),
    path('delete_success/', views.delete_success, name="delete_success"),
    path('add/', views.add, name="add"),
    path('delete/', views.delete, name="delete")
]