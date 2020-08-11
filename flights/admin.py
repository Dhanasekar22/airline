from django.contrib import admin

from .models import *

# Register your models here.
class FlightsAdmin(admin.ModelAdmin):
    list_display=("id","origin","destination","duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)

admin.site.register(Airport)
admin.site.register(Flights,FlightsAdmin)
admin.site.register(Passenger,PassengerAdmin)