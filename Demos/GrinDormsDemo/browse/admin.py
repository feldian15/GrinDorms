from django.contrib import admin

from .models import Room, Building

# Register your models here.
admin.site.register(Building)
admin.site.register(Room)

