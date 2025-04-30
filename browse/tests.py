from django.test import TestCase
from .models import Room, Building, Floors
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

    def test_correct_floors(self):
        test_building = Building(name="TESTBLD", num_floors=3, has_pit=True)
        test_building.save()

        # make sure the highest floor is the second floor
        floor_list = test_building.get_floor_list()

        # top floor value should be the number of floors minus 1
        self.assertIs(floor_list[test_building.num_floors - 1][0], test_building.num_floors - 1)
    
    def test_valid_floor_number(self):
        test_building = Building(name="TESTBLD", num_floors=3, has_pit=True)
        test_building.save()

        # make a room on the third floor of a building with only 2 floors above ground
        test_third_floor_room = Room(building=test_building, number=3300)

        try:
            test_third_floor_room.save()
        except ValueError:
            caught1 = True
        else:
            caught1 = False
        
        test_building_2 = Building(name="TESTBLD2", num_floors=3, has_pit=False)
        test_building_2.save()

        # make a room in the pit of the building without a pit
        test_pit_room = Room(building=test_building_2, number=3001)

        try:
            test_pit_room.save()
        except ValueError:
            caught2 = True
        else:
            caught2 = False

        self.assertIs((caught1 and caught2), True)
