from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=140)

class Lead(models.Model):
    summary = models.CharField(max_length=140, help_text="Describe it in a tweet or less")
    description = models.TextField(null=True, blank=True, help_text="More details go here")
    date_entered = models.DateField(auto_now_add=True)
    date_due = models.DateField(blank=True, null=True)
    entered_by = models.ForeignKey('auth.User', related_name="lead_entered_by", null=True, blank=True)
    assigned_to = models.ForeignKey('auth.User', related_name="lead_assigned_to", null=True, blank=True)
    contact_name = models.CharField(max_length=140, help_text="Who can we contact about this?", blank=True, null=True)
    contact_email = models.CharField(max_length=140, help_text="What's their email address?", blank=True, null=True)
    event_date = models.DateField(blank=True, null=True, help_text="Does this lead have an exipration?")
    notes = models.TextField(null=True, blank=True, help_text="Anything else?")
    lead_category = models.ManyToManyField(Category)
