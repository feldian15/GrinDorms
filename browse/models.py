from django.db import models
from django.db.models import Avg

MAXLEN = 50

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
    FIVEMAN = 5, "Five-Person"
    SIXMAN = 6, "Six-Person"
    SEVENMAN = 7, "Seven-Person"

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
    num_floors = models.IntegerField(default=1)
    has_pit = models.BooleanField(default=False)
    num_kitchens = models.IntegerField(default=1)
    central_ac = models.BooleanField(default=False)
    num_washers = models.IntegerField(default=1)
    num_dryers = models.IntegerField(default=1)
    elevator = models.BooleanField(default=False)
    gender_specific = models.BooleanField(default=False)
    sub_free = models.BooleanField(default=False)

    def __str__ (self):
        return self.name
    
    def get_floor_list(self):
        if self.has_pit:
            return Floors.choices[0:self.num_floors]
        else:
            return Floors.choices[1:self.num_floors + 1]
        
    def display_building_name(self):
        return self.name.title() + " Hall"

class Room(models.Model):
    building = models.ForeignKey(Building, related_name="rooms", on_delete=models.CASCADE)
    number = models.IntegerField(default = 1111)
    floor = models.IntegerField(editable=False, choices=Floors.choices, default=Floors.PIT)
    num_occupants = models.IntegerField(choices=Sizes.choices, default=Sizes.SINGLE)
    floor_bathrooms = models.IntegerField(default=1)
    multi_room = models.BooleanField(default=True)
    srd = models.BooleanField(default=False)
    internal_bathroom = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    ca = models.BooleanField(default=False)
    avg_rating = models.FloatField(default=0.0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['building', 'number'],
                name = 'unique room in building'
            )
        ]

    def display_room_number(self):
        if self.building.name == "RENFROW":
            # Get first digit 1=N, 2=S, 3=W
            lead_digit = int(self.number / 1000)
            remainder = self.number % 1000
            if lead_digit == 1:
                return f'N{remainder}'
            elif lead_digit == 2:
                return f'S{remainder}'
            else:
                return f'W{remainder}'
        else:
            return str(self.number)
        

    def __str__ (self):
        return "%s %s" % (self.building.name, self.number)
    
    def save(self, *args, **kwargs):
        # Check that the room number is 4 digits
        if not (100 <= self.number <= 9999):
            raise ValueError("Room number must be a 3 or 4-digit number.")
        
        # set the floor based on the second digit of the room number
        temp = str(self.number)
        self.floor = int(temp[1:2])

        # check that the floor exists in the building
        if (self.building.has_pit and self.floor >= self.building.num_floors) or ((not self.building.has_pit) and self.floor > self.building.num_floors):
            raise ValueError("Building %s has %d floors above ground. Room claims to be on floor %d." % (self.building.name, self.building.num_floors, self.floor))
        if (not self.building.has_pit) and self.floor == 0:
            raise ValueError("Building %s has no pit" % self.building.name)
        
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