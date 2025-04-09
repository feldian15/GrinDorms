from datetime import timezone
from django.db import models
from browse.models import Room
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

MAXLEN = 200
class Ratings(models.IntegerChoices):
    AWFUL = 1, 'Awful'
    POOR = 2, 'Poor'
    OKAY = 3, 'Okay'
    GOOD = 4, 'Good'
    AWESOME = 5, 'Awesome'



# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE, default=1)
    created_time = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Ratings.choices, default=Ratings.OKAY)
    text = models.CharField(max_length=MAXLEN)
    display = models.BooleanField(default=True)

    def __str__ (self):
        return "%s %d review by %s" % (self.room.building.name, self.room.number, self.user.username)

class Image(models.Model):
    review = models.ForeignKey(Review, related_name="images", on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='review_images/', blank=True, null=True)

    def __str__ (self):
        return "%s %d review image" % (self.review.room.building.name, self.review.room.number)
    

# function to delete all associated images from media folder whenever a review is deleted
@receiver(post_delete, sender=Image)
def delete_image_file(sender, instance, **kwargs):
    # Check for the image path
    if instance.image_url and instance.image_url.path:
        # ensure it's a file
        if os.path.isfile(instance.image_url.path):
            # remove it
            os.remove(instance.image_url.path)