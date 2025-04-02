from django.db import models

MAXLEN = 50

# Create your models here.
class Building(models.model):
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
