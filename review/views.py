from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# View for adding a new review
def review(request):
    return HttpResponse("This is the page for reviewing")

# view for viewing user specific reviews
def my_reviews(request):
    return HttpResponse("This is the page for viewing my reviews")

# view after a successful add
def add_success(request):
    return HttpResponse("This is the page after submitting a review successfully")

# view after a successful delete
def delete_success(request):
    return HttpResponse("This is the page after a successful deletion")

# logic to handle post request to add
def add(request):
    return HttpResponseRedirect(reverse("review:add_success"))

# logic to handle post request to delete
def delete(request):
    return HttpResponseRedirect(reverse("review:delete_success"))