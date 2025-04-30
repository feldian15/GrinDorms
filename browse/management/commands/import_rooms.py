import csv
from django.core.management.base import BaseCommand
from browse.models import Room, Building, Regions
from django.db.utils import IntegrityError
import os

class Command(BaseCommand):
    help = 'Imports buildings data from a CSV file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'Grinnell College Dorms.csv')

        with open(file_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Map CSV values to the correct model fields
                building_name=row['building']
                building = Building.objects.get(name=building_name)
                room = Room(
                    building=building,
                    number=int(row['number']),
                    num_occupants=int(row['num_occupants_2025']),
                    floor_bathrooms=int(row['floor_bathrooms']),
                    srd=True if row['srd'] == 't' else False,
                    internal_bathroom=True if row['internal_bathroom'] == 't' else False,
                    kitchen=True if row['kitchen'] == 't' else False,
                    available=True if row['available'] == 't' else False,
                    ca=True if row['ca'] == 't' else False
                )

                room.save()