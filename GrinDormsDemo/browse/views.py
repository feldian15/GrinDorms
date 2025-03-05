from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Building, Room

# Create your views here.

def home(request):
    building_list = Building.objects.order_by("name")
    context = {"building_list": building_list}
    return render(request, "browse/home.html", context)

def floors(request, building_name):
    #get the associated building
    building = get_object_or_404(Building, name = building_name)
    
    num_floors = building.num_floors
    has_pit = building.has_pit

    #if the building has a pit, remove one of the floors
    if(has_pit):
        floor_list = range(0, num_floors)
    else:
        floor_list = range(1, num_floors + 1)

    context = {"floor_list": floor_list,
               "building_name": building.name}

    return render(request, "browse/floors.html", context)

def rooms(request, building_name, floor_num):
    #get the associated building
    building = get_object_or_404(Building, name = building_name)

    room_list = Room.objects.filter(floor = floor_num, building = building)

    context = {"floor_num": floor_num,
               "building_name": building.name,
               "room_list": room_list}

    return render(request, "browse/rooms.html", context)

def rooms_updated(request, args):
    # Parse out all of the filter arguments
    region_list = ["NORTH", "EAST", "SOUTH"]
    building_list = Building.objects.all()
    floor_list = ["PIT", "1", "2", "3", "4"]
    room_list = Room.objects.all()

    context = {"region_list": region_list,
               "building_list": building_list,
               "floor_list": floor_list,
               "room_list": room_list}

    return render(request, "browse/rooms_updated.html", context)

def room_details(request, building_name, floor_num, room_number):
    return HttpResponse("This is the view of the details of room %d on floor %d of %s Hall" % (room_number, floor_num, building_name))
