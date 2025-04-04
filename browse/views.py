from django.shortcuts import render, HttpResponse
from . models import Room, Building
from review.models import Review, Image

# Create your views here.
# View for browse filtering and sorting
def browse(request):
    # filtering criteria are region, building, floor, srd, size, 
    # direction, washers, dryers, elevator, gender specific, rating...

    # Get the full set of rooms first
    room_list = Room.objects.all()

    
    
    # Filter the room list based on any selected criteria

    # Ensure selected criteria is passed back to the template

    # (re)render the template
    return HttpResponse("This is the browse page")

# View for a specific room's details and reviews
def room_details(request, building_name, room_number):
    return HttpResponse("This is the details page for room %d of %s Hall" % (room_number, building_name))