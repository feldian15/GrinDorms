from django.test import TestCase
from .models import Room, Building
from django.db.utils import IntegrityError

# Create your tests here.
class RoomModelTests(TestCase):
    def test_no_duplicate_floors(self):
        # Check to ensure all rooms are unique in their building
        test_building = Building(name="TESTBLD", num_floors=3, has_pit=True)
        test_building.save()

        test_room_1 = Room(building=test_building, number=1111)
        test_room_2 = Room(building=test_building, number=1111)

        test_room_1.save()

        # Should raise an IntegrityError
        try:
            test_room_2.save()
        except IntegrityError:
            caught = True
        else:
            caught = False
        
        self.assertIs(caught, True)


