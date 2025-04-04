from django.db import models
from browse.models import Room

MAXLEN = 200

# Create your models here.
class Review(models.Model):
    RATING_OPTIONS = [(1, "awful"), (2, "poor"), (3, "okay"), (4, "good"), (5, "great")]

    room = models.ForeignKey(Room, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_OPTIONS)
    text = models.CharField(max_length=MAXLEN)
    display = models.BooleanField(default=True)

    def __str__ (self):
        return "%s %d review" % (self.room.building.name, self.room.number)

class Image(models.Model):
    review = models.ForeignKey(Review, related_name="images", on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='review_images/', blank=True, null=True)

    def __str__ (self):
        return "%s %d review image" % (self.review.room.building.name, self.review.room.number)