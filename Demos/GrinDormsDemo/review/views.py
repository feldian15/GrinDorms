from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db.models import F

from .models import Review
from browse.models import Room, Building

# Create your views here.

def review(request):
    building_list = Building.objects.all()
    room_list = Room.objects.all()

    context = {
        "building_list": building_list,
        "room_list": room_list
    }
    
    return render(request, "review/review.html", context)
