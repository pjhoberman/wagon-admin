from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=140)
    date = models.DateField()

    def __unicode__(self):
        return "%s (%s)" % (self.name, str(self.date))

class Volunteer(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    email = models.CharField(max_length=140)
    phone = models.CharField(max_length=140, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    volunteered_at = models.ManyToManyField(Event, blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
