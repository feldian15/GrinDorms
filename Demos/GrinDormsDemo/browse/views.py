from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import re

from .models import Building, Room
from review.models import Review, Image

# Create your views here.

def rooms(request):
    selected_regions = request.GET.getlist('region')
    selected_buildings = request.GET.getlist('building')
    selected_floors = request.GET.getlist('floor')
    sort = request.GET.get('sort')

    selected_floors_filter = ["0" if item == "PIT" else item for item in selected_floors]

    if selected_regions:
        room_list = Room.objects.filter(building__region__in=selected_regions)
    if selected_buildings:
        room_list = Room.objects.filter(building__name__in=selected_buildings)
    if selected_floors:
        room_list = Room.objects.filter(floor__in=selected_floors_filter)
    if not (selected_regions or selected_buildings or selected_floors):
        room_list = Room.objects.all()
    if sort == "asc":
        room_list = room_list.order_by('avg_rating')
    if sort == "desc":
        room_list = room_list.order_by('-avg_rating')

        
    region_list = ["NORTH", "EAST", "SOUTH"]
    building_list = Building.objects.all()
    floor_list = ["PIT", "1", "2", "3", "4"]

    context = {"selected_regions": selected_regions,
               "region_list": region_list,
               "selected_buildings": selected_buildings,
               "building_list": building_list,
               "selected_floors": selected_floors,
               "floor_list": floor_list,
               "room_list": room_list,
               "sort": sort}

    return render(request, "browse/rooms.html", context)

def room_details(request, building_name, room_number):
    room = Room.objects.get(building__name=building_name, number=room_number)
    review_list = Review.objects.filter(room=room)
    image_list = Image.objects.filter(review__room=room)

    context = {"room": room,
               "review_list": review_list,
               "image_list": image_list}
    
    return render(request, "browse/room_details.html", context)