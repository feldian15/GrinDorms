from django.db import models
from django.db.models import Avg

MAXLEN = 50

class Directions(models.TextChoices):
    NORTH = "N", 'North'
    SOUTH = "S", 'South'
    EAST = "E", 'East'
    WEST = "W", 'West'

class Regions(models.TextChoices):
    NORTH = "N", "North"
    EAST = "E", "East"
    SOUTH = "S", "South"
    OFF = "O", "Off-Campus"

class Sizes(models.IntegerChoices):
    SINGLE = 1, "Single"
    DOUBLE = 2, "Double"
    TRIPLE = 3, "Triple"
    QUAD = 4, "Quad"
    FIVEMAN = 5, "Five-man"
    SIXMAN = 6, "Six-man"
    SEVENMAN = 7, "Seven-man"

class Floors(models.IntegerChoices):
    PIT = 0, "Pit"
    FIRST_FLOOR = 1, 'First Floor'
    SECOND_FLOOR = 2, 'Second Floor'
    THIRD_FLOOR = 3, 'Third Floor'
    FOURTH_FLOOR = 4, 'Fourth Floor'

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=MAXLEN)
    region = models.CharField(max_length=1, choices=Regions.choices, default=Regions.NORTH)
    num_floors = models.IntegerField()
    has_pit = models.BooleanField()
    num_kitchens = models.IntegerField()
    central_ac = models.BooleanField()
    num_washers = models.IntegerField()
    num_dryers = models.IntegerField()
    elevator = models.BooleanField()
    gender_specific = models.BooleanField()
    sub_free = models.BooleanField(default=False)

    def __str__ (self):
        return self.name

class Room(models.Model):
    building = models.ForeignKey(Building, related_name="rooms", on_delete=models.CASCADE)
    number = models.IntegerField()
    floor = models.IntegerField(editable=False, choices=Floors.choices, default=Floors.PIT)
    num_occupants = models.IntegerField(choices=Sizes.choices, default=Sizes.SINGLE)
    window_direction = models.CharField(choices=Directions.choices, default=Directions.NORTH, max_length=1)
    floor_bathrooms = models.IntegerField()
    srd = models.BooleanField()
    internal_bathroom = models.BooleanField()
    kitchen = models.BooleanField()
    common_room = models.BooleanField()
    avg_rating = models.FloatField(default=0.0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['building', 'number'],
                name = 'unique room in building'
            )
        ]

    def __str__ (self):
        return "%s %d" % (self.building.name, self.number)
    
    def save(self, *args, **kwargs):
        # Check that the room number is 4 digits
        if not (1000 <= self.number <= 9999):
            raise ValueError("Room number must be a 4-digit number.")
        # set the floor based on the second digit of the room number
        temp = str(self.number)
        self.floor = int(temp[1:2])
        super().save(*args, **kwargs)

    # method to calculate the average rating from all reviews of the room
    def calc_avg_rating(self):
        avg = self.reviews.aggregate(Avg('rating'))['rating__avg']
        self.avg_rating = round(avg or 0.0, 2)
        self.save()
        # temp_avg_rating = 0.0
        # num_reviews = self.reviews.count()
        # # Check if the room has reviews
        # if num_reviews > 0:
        #     # find the average
        #     for review in self.reviews.all():
        #         temp_avg_rating += review.rating

        #     temp_avg_rating = temp_avg_rating / num_reviews

        #     self.avg_rating = round(temp_avg_rating, 2)
        # else:
        #     self.avg_rating = 0.0
        
        # # save the new average
        # self.save()