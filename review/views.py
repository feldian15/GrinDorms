from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from browse.models import Room, Building, Regions
from .models import Review, Image

# Create your views here.
# View for adding a new review
def review(request):
    # get input params
    selected_region = request.GET.get("region")
    selected_building = request.GET.get("building")
    selected_floor = request.GET.get("floor")
    if selected_floor:
        selected_floor = int(selected_floor)

    building_list = Building.objects.filter(region=selected_region)

    if selected_building:
        floor_list = Building.objects.get(name=selected_building).get_floor_list
    else: 
        floor_list = []
    
    if selected_floor or selected_floor == 0:
        room_list = Room.objects.filter(floor=selected_floor, building__name = selected_building)
    else:
        room_list = []

    selected_room = int(request.GET.get('room')) if request.GET.get('room') and request.GET.get('room') != 'none' else 0

    context = {
        "region_list": Regions.choices,
        "building_list": building_list,
        # This doesn't keep track of which buildings have pits etc
        "floor_list": floor_list,
        "room_list": room_list,
        "selected_region": selected_region,
        "selected_building": selected_building,
        "selected_floor": selected_floor,
        "selected_room": selected_room
    }

    return render(request, "review/review.html", context)

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