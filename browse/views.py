from django.shortcuts import render, HttpResponse
from . models import Room, Building, Regions, Sizes, Floors
from review.models import Review, Image
from django.contrib.auth.decorators import login_required

# Set up all the filtering lists
BUILDING_LIST = Building.objects.all()


# Create your views here.
# View for browse filtering and sorting
@login_required(login_url="login:my-login")
def browse(request):
    # filtering criteria are region, building, floor, srd, size, 
    # direction, washers, dryers, elevator, gender specific, rating...
    
    # get all the filters
    selected_regions = request.GET.getlist("region")
    selected_buildings = request.GET.getlist("building")

    # turn requests into integers
    selected_floors = request.GET.getlist("floor")
    selected_floors = [int(x) for x in selected_floors]
    selected_sizes = request.GET.getlist("size")
    selected_sizes = [int(x) for x in selected_sizes]

    sub_free = request.GET.get("sub_free")
    elevator = request.GET.get("elevator")
    women_only = request.GET.get("women_only")
    srd = request.GET.get("srd")
    ca = request.GET.get("ca")
    rating = request.GET.get("rating")

    # Get the full set of rooms first
    room_list = Room.objects.all()

    # Filter the room list based on any selected criteria
    if selected_regions:
        room_list = room_list.filter(building__region__in=selected_regions)
    if selected_buildings:
        room_list = room_list.filter(building__name__in=selected_buildings)
    if selected_floors:
        room_list = room_list.filter(floor__in=selected_floors)
    if selected_sizes:
        room_list = room_list.filter(num_occupants__in=selected_sizes)
    if sub_free:
        room_list = room_list.filter(building__sub_free=sub_free)
    if elevator:
        room_list = room_list.filter(building__elevator=elevator)
    if women_only:
        room_list = room_list.filter(building__gender_specific=women_only)
    if srd:
        room_list = room_list.filter(srd=srd)
    if ca:
        room_list = room_list.filter(ca=ca)
    if rating == 'asc':
        room_list = room_list.order_by('avg_rating')
    if rating == 'desc':
        room_list = room_list.order_by('-avg_rating')

    # Ensure selected criteria is passed back to the template
    context = {
        "selected_regions": selected_regions,
        "selected_buildings": selected_buildings,
        "selected_floors": selected_floors,
        "selected_sizes": selected_sizes,
        "sub_free": sub_free,
        "elevator": elevator,
        "women_only": women_only,
        "srd": srd,
        "ca": ca,
        "rating": rating,
        "room_list": room_list,
        "building_list": BUILDING_LIST,
        "floor_list": Floors.choices,
        "region_list": Regions.choices,
        "size_list": Sizes.choices
    }

    # (re)render the template
    return render(request, "browse/rooms.html", context)

# View for a specific room's details and reviews
@login_required(login_url="login:my-login")
def room_details(request, building_name, room_number):
    # get the room
    room = Room.objects.get(building__name=building_name, number=room_number)

    # find the associated reviews and images
    review_list = Review.objects.filter(room=room)
    image_list = Image.objects.filter(review__room=room)

    context = {
        "room": room,
        "review_list": review_list,
        "image_list": image_list
    }

    return render(request, "browse/room_details.html", context)