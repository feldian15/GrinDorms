from django.db import models

MAXLEN = 50

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=MAXLEN)
    region = models.CharField(max_length=MAXLEN)
    num_floors = models.IntegerField()
    has_pit = models.BooleanField()
    num_kitchens = models.IntegerField()
    central_ac = models.BooleanField()
    num_washers = models.IntegerField()
    num_dryers = models.IntegerField()
    elevator = models.BooleanField()
    gender_specific = models.BooleanField()

    def __str__ (self):
        return self.name()

class Room(models.Model):
    building = models.ForeignKey(Building, related_name="rooms", on_delete=models.CASCADE)
    number = models.IntegerField()
    floor = models.IntegerField(editable=False)
    num_occupants = models.IntegerField()
    window_direction = models.IntegerChoices
    floor_bathrooms = models.IntegerField()
    srd = models.BooleanField()
    internal_bathroom = models.BooleanField()
    kitchen = models.BooleanField()
    common_room = models.BooleanField()

    def __str__ (self):
        return "building.name %d" % self.number
