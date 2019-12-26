from django.contrib import admin

from .models import Room, Review, Booking, Question

admin.site.register(Room)
admin.site.register(Review)
admin.site.register(Booking)
admin.site.register(Question)
