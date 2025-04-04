from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Review, Image
from browse.models import Room, Building

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
    review_list = Review.objects.filter(display=True).prefetch_related("images")
    deleted_flag = request.GET.get("deleted") == "true"

    context = {
        "review_list": review_list,
        "show_deleted_popup": deleted_flag
    }

    return render(request, "review/my_reviews.html", context)

def add(request, building_name, room_number):
    stars = int(request.POST.get("stars", 0))
    review_text = request.POST.get("review_text")

    room = Room.objects.get(building__name=building_name, number=room_number)

    new_review = Review(room=room, rating=stars, comments=review_text)
    new_review.save()

    room.calc_avg_rating()

    for image in request.FILES.getlist("image"):
        new_image = Image(review=new_review, data=image)
        new_image.save()

    return HttpResponseRedirect(reverse("review:review_added"))

def review_added(request):
    return render(request, "review/review_added.html", {})

def remove_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    room = review.room

    review.delete()
    room.calc_avg_rating()

    return redirect('/review/myreviews?deleted=true')
