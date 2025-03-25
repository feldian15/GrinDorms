from django.db import models

MAXLEN = 50

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length = MAXLEN)
    cluster = models.CharField(max_length = MAXLEN)
    region = models.CharField(max_length = MAXLEN)
    num_floors = models.IntegerField(default = 0)
    has_pit = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Room(models.Model):
    building = models.ForeignKey(Building, related_name="rooms", on_delete=models.CASCADE)
    floor = models.IntegerField(editable = False)
    number = models.IntegerField(default = 0000)
    avg_rating = models.FloatField(default = 0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['building', 'number'],
                name = 'unique_room_in_building'
            )
        ]

    def save(self, *args, **kwargs):
        temp = str(self.number)
        self.floor = int(temp[1:2])
        super().save(*args, **kwargs)

    
    def __str__(self):
        br = "%s %d" % (self.building.name, self.number)
        return br
    
    @property
    def floor_display(self):
        return "PIT" if self.floor == 0 else str(self.floor)
    
    def calc_avg_rating(self):
        if self.reviews.count() > 0:
            avg_rating_temp = 0
            for review in self.reviews.all():
                avg_rating_temp += review.rating
        
            avg_rating_temp = avg_rating_temp / self.reviews.count()
        
            self.avg_rating = round(avg_rating_temp, 2)
        else:
            self.avg_rating = 0.0
        
        self.save()