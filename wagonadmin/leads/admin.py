from django.contrib import admin
from leads.models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('summary', 'date_entered', 'date_due', 'entered_by', 'assigned_to')

admin.site.register(Lead, LeadAdmin)
