from django.shortcuts import render, HttpResponse

# Create your views here.
# View for browse filtering and sorting
def browse(request):
    return HttpResponse("This is the browse page")

# View for a specific room's details and reviews
def room_details(request, building_name, room_number):
    return HttpResponse("This is the details page for room %d of %s Hall" % (room_number, building_name))