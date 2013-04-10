from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
from volunteers.models import Event, Volunteer

class VolunteerAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Event, EventAdmin)
