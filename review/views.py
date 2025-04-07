from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from browse.models import Room, Building, Regions
from .models import Review, Image

# Create your views here.
# View for adding a new review
def review(request):
    # get input params
    selected_region = request.GET.get("region")
    selected_building = request.GET.get("building")
    selected_floor = request.GET.get("floor")
    if selected_floor:
        selected_floor = int(selected_floor)

    building_list = Building.objects.filter(region=selected_region)

    if selected_building:
        floor_list = Building.objects.get(name=selected_building).get_floor_list
    else: 
        floor_list = []
    
    if selected_floor or selected_floor == 0:
        room_list = Room.objects.filter(floor=selected_floor, building__name = selected_building)
    else:
        room_list = []

    selected_room = int(request.GET.get('room')) if request.GET.get('room') and request.GET.get('room') != 'none' else 0

    context = {
        "region_list": Regions.choices,
        "building_list": building_list,
        # This doesn't keep track of which buildings have pits etc
        "floor_list": floor_list,
        "room_list": room_list,
        "selected_region": selected_region,
        "selected_building": selected_building,
        "selected_floor": selected_floor,
        "selected_room": selected_room
    }

    return render(request, "review/review.html", context)

# view for viewing user specific reviews
def my_reviews(request):
    # Get reviews 
    # NEED TO MAKE THIS USER SPECIFIC
    review_list = Review.objects.filter(display=True)

    # Grab any associated images
    review_list = review_list.prefetch_related("images")

    context = {"review_list": review_list}

    return render(request, "review/my_reviews.html", context)

# view after a successful add
def add_success(request):
    return render(request, "review/add_success.html", {})

# view after a successful delete
def delete_success(request):
    return render(request, "review/delete_success.html", {})

# logic to handle post request to add
def add(request, building_name, room_number):
    # grab the non image related fields
    rating = request.POST.get("stars")
    review_text = request.POST.get("review_text")

    # Get the associated room
    room = Room.objects.get(building__name=building_name, number=room_number)

    # make the new review:
    new_review = Review(room=room, rating=rating, text=review_text)
    new_review.save()

    # update the rating on the room
    room.calc_avg_rating()

    # Image handing
    image_list = request.FILES.getlist("image")

    # save all new images
    for image in image_list:
        new_image = Image(review=new_review, image_url=image)
        new_image.save()

    # redirect to the success screen
    return HttpResponseRedirect(reverse("review:add_success"))

# logic to handle post request to delete
def delete(request):
    # get the id of the review to delete
    review_id = request.POST.get("review_id")
    review = Review.objects.get(id=review_id)

    # find the room to recalculate the ratings
    room = review.room

    # delete the the review
    review.delete()

    # recalculate the average rating
    room.calc_avg_rating()

    # redirect to a success message
    return HttpResponseRedirect(reverse("review:delete_success"))