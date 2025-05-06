import csv
from django.core.management.base import BaseCommand
from browse.models import Building, Regions
from django.db.utils import IntegrityError
import os

class Command(BaseCommand):
    help = 'Imports buildings data from a CSV file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'Grinnell College Buildings.csv')

        with open(file_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Map CSV values to the correct model fields
                building = Building(
                    name=row['name'],
                    region=row['region'],
                    num_floors=int(row['num_floors']),
                    has_pit=True if row['has_pit'] == 't' else False,
                    num_kitchens=int(row['num_kitchens']),
                    central_ac=True if row['central_ac'] == 't' else False,
                    num_washers=int(row['num_washers']),
                    num_dryers=int(row['num_dryers']),
                    elevator=True if row['elevator'] == 't' else False,
                    gender_specific=True if row['gender_specific'] == 't' else False,
                    sub_free=True if row['sub_free'] == 't' else False,
                )

                building.save()