from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db.models import F

from .models import Review, Image
from browse.models import Room, Building

# Create your views here.

def review(request):
    building_list = Building.objects.all()
    selected_building = request.GET.get('building')
    floor_list = []

    if selected_building:
        b = Building.objects.get(name=selected_building)
        if b.has_pit:
            for i in range(0, b.num_floors):
                floor_list.append(str(i))
            floor_list[0] = "PIT"
        else:
            for i in range(0, b.num_floors):
                floor_list.append(str(i + 1))

    selected_floor = request.GET.get('floor')
    if selected_floor == "PIT":
        selected_floor_filter = 0
    else:
        selected_floor_filter = selected_floor

    if selected_floor:
        room_list = Room.objects.filter(building__name=selected_building, floor=selected_floor_filter)
    else:
        room_list = []

    selected_room = int(request.GET.get('room')) if request.GET.get('room') and request.GET.get('room') != 'none' else 0
    
    
    context = {
        "selected_building": selected_building,
        "building_list": building_list,
        "selected_floor": selected_floor,
        "floor_list": floor_list,
        "selected_room": selected_room,
        "room_list": room_list
    }
            
    return render(request, "review/review.html", context)

def my_reviews(request):
    review_list = Review.objects.filter(display=True)
    review_list = review_list.prefetch_related("images")

    context = {"review_list": review_list}

    return render(request, "review/my_reviews.html", context)

def add(request, building_name, room_number):
    stars = 0
    if request.POST.get("stars"):
        stars = int(request.POST.get("stars"))

    review_text = request.POST.get("review_text")

    room = Room.objects.get(building__name=building_name, number=room_number)

    new_review = Review()
    new_review.room = room
    new_review.rating = stars
    new_review.comments = review_text

    new_review.save()

    room.calc_avg_rating()

    image_data = request.FILES.getlist("image")

    for image in image_data:
        new_image = Image()
        new_image.review = new_review
        new_image.data = image

        new_image.save()

    return HttpResponseRedirect(reverse("review:review_added"))

def remove(request):
    review_id = request.POST.get("review_id")

    review = Review.objects.get(id=review_id)

    room = review.room

    # Make sure to delete urls from the media folder

    review.delete()

    room.calc_avg_rating()

    return HttpResponseRedirect(reverse("review:review_removed"))

def review_added(request):
    return render(request, "review/review_added.html", {})

def review_removed(request):
    return render(request, "review/review_removed.html", {})
