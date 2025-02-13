from django.db import models

MAXLEN = 50

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length = MAXLEN)
    cluster = models.CharField(max_length = MAXLEN)
    region = models.CharField(max_length = MAXLEN)

    def __str__(self):
        return self.name

class Floor(models.Model):
    building = models.ForeignKey(Building, related_name="floors", on_delete=models.CASCADE)
    number = models.IntegerField(default = 0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['building', 'number'],
                name = 'unique_floor_in_building'
            )
        ]

    def __str__(self):
        bf = "%s, floor %d" % (self.building.name, self.number)
        return bf

class Room(models.Model):
    building = models.ForeignKey(Building, related_name="rooms", on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, related_name="rooms", on_delete=models.CASCADE)
    number = models.IntegerField(default = 0000)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['floor', 'number'],
                name = 'unique_room_on_floor'
            ),
            models.UniqueConstraint(
                fields = ['building', 'number'],
                name = 'unique_room_in_building'
            )
        ]

    def __str__(self):
        br = "%s %d" % (self.building.name, self.number)
        return br