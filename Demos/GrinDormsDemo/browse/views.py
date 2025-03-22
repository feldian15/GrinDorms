from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import re

from .models import Building, Room

# Create your views here.

def rooms(request):
    selected_regions = request.GET.getlist('region')
    selected_buildings = request.GET.getlist('building')
    selected_floors = request.GET.getlist('floor')
    selected_floors_filter = ["0" if item == "PIT" else item for item in selected_floors]

    if selected_regions:
        room_list = Room.objects.filter(building__region__in=selected_regions)
    if selected_buildings:
        room_list = Room.objects.filter(building__name__in=selected_buildings)
    if selected_floors:
        room_list = Room.objects.filter(floor__in=selected_floors_filter)
    if not (selected_regions or selected_buildings or selected_floors):
        room_list = Room.objects.all()

        
    region_list = ["NORTH", "EAST", "SOUTH"]
    building_list = Building.objects.all()
    floor_list = ["PIT", "1", "2", "3", "4"]

    context = {"selected_regions": selected_regions,
               "region_list": region_list,
               "selected_buildings": selected_buildings,
               "building_list": building_list,
               "selected_floors": selected_floors,
               "floor_list": floor_list,
               "room_list": room_list}

    return render(request, "browse/rooms.html", context)

def room_details(request, building_name, floor_num, room_number):
    return HttpResponse("This is the view of the details of room %d on floor %d of %s Hall" % (room_number, floor_num, building_name))

# def home(request):
#     building_list = Building.objects.order_by("name")
#     context = {"building_list": building_list}
#     return render(request, "browse/home.html", context)

# def floors(request, building_name):
#     #get the associated building
#     building = get_object_or_404(Building, name = building_name)
    
#     num_floors = building.num_floors
#     has_pit = building.has_pit

#     #if the building has a pit, remove one of the floors
#     if(has_pit):
#         floor_list = range(0, num_floors)
#     else:
#         floor_list = range(1, num_floors + 1)

#     context = {"floor_list": floor_list,
#                "building_name": building.name}

#     return render(request, "browse/floors.html", context)

# def rooms(request, building_name, floor_num):
#     #get the associated building
#     building = get_object_or_404(Building, name = building_name)

#     room_list = Room.objects.filter(floor = floor_num, building = building)

#     context = {"floor_num": floor_num,
#                "building_name": building.name,
#                "room_list": room_list}

#     return render(request, "browse/rooms.html", context)