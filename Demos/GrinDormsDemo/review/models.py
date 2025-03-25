from django.db import models
from browse.models import Room

# Create your models here.
MAXLEN = 500

class Review(models.Model):
    RATING_OPTIONS = [
        (1, "Awful"),
        (2, "Poor"),
        (3, "Fair"),
        (4, "Good"),
        (5, "Awesome")
    ]

    room = models.ForeignKey(Room, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_OPTIONS, default = 3)
    comments = models.CharField(max_length=MAXLEN)
    display = models.BooleanField(default = True)

    def __str__(self):
        return "%s Hall room %d review" % (self.room.building.name, self.room.number)
    
class Image(models.Model):
    review = models.ForeignKey(Review, related_name="images", on_delete=models.CASCADE)
    data = models.ImageField(upload_to='review_images/', blank=True, null=True)

    def __str__(self):
        return str(self.review.room.number) + "review image"