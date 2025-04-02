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
        # set the floor based on the second digit of the room number
        temp = str(self.number)
        self.floor = int(temp[1:2])
        super().save(*args, **kwargs)

    # method to calculate the average rating from all reviews of the room
    def calc_avg_rating(self):
        temp_avg_rating = 0.0
        num_reviews = self.reviews.count()
        # Check if the room has reviews
        if num_reviews > 0:
            # find the average
            for review in self.reviews.all():
                temp_avg_rating += review.rating

            temp_avg_rating = temp_avg_rating / num_reviews

            self.avg_rating = round(temp_avg_rating, 2)
        else:
            self.avg_rating = 0.0
        
        # save the new average
        self.save()