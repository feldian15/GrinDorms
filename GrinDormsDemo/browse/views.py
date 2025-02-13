from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Building, Floor, Room

# Create your views here.

def home(request):
    building_list = Building.objects.order_by("name")
    context = {"building_list": building_list}
    return render(request, "browse/home.html", context)

def floors(request, building_name):
    #get the associated building
    building = get_object_or_404(Building, name = building_name)

    #get the floors for this building
    floor_list = Floor.objects.filter(building = building)

    context = {"building_name": building.name,
               "floor_list": floor_list}
    
    return render(request, "browse/floors.html", context)

def rooms(request, building_name, floor_number):
    #get the associated building
    building = get_object_or_404(Building, name = building_name)

    #get the associated floor
    floor = get_object_or_404(Floor, number = floor_number)

    #get the associated rooms
    room_list = Room.objects.filter(building = building, floor = floor)

    context = {"building_name": building.name,
               "floor_number": floor.number,
               "room_list": room_list}

    return render(request, "browse/rooms.html", context)

def room_details(request, building_name, floor_number, room_number):
    return HttpResponse("This is the view of the details of room %d on floor %d of %s Hall" % (room_number, floor_number, building_name))
