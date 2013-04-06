from django.db import models

class Lead(models.Model):
    summary = models.CharField(max_length=140, help_text="Describe it in a tweet or less")
    description = models.TextField(null=True, blank=True, help_text="More details go here")
    date_entered = models.DateField(auto_now_add=True)
    date_due = models.DateField(blank=True, null=True)
    entered_by = models.ForeignKey('auth.User', related_name="lead_entered_by", null=True, blank=True)
    assigned_to = models.ForeignKey('auth.User', related_name="lead_assigned_to", null=True, blank=True)
