from django.contrib import admin

from .models import *
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Message)
admin.site.register(Booking)
admin.site.register(Review)

