from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
from leads.models import Lead, Category

class LeadAdmin(admin.ModelAdmin):
    list_display = ('summary', 'date_entered', 'date_due', 'entered_by', 'assigned_to')
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lead, LeadAdmin)
admin.site.register(Category, CategoryAdmin)
