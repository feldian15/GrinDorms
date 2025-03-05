from django.db import models
from browse.models import Room

# Create your models here.
MAXLEN = 200

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

    def __str__(self):
        return self.room + "review"