# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'volunteers_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'volunteers', ['Event'])

        # Adding model 'Volunteer'
        db.create_table(u'volunteers_volunteer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'volunteers', ['Volunteer'])

        # Adding M2M table for field volunteered_at on 'Volunteer'
        db.create_table(u'volunteers_volunteer_volunteered_at', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('volunteer', models.ForeignKey(orm[u'volunteers.volunteer'], null=False)),
            ('event', models.ForeignKey(orm[u'volunteers.event'], null=False))
        ))
        db.create_unique(u'volunteers_volunteer_volunteered_at', ['volunteer_id', 'event_id'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'volunteers_event')

        # Deleting model 'Volunteer'
        db.delete_table(u'volunteers_volunteer')

        # Removing M2M table for field volunteered_at on 'Volunteer'
        db.delete_table('volunteers_volunteer_volunteered_at')


    models = {
        u'volunteers.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'volunteers.volunteer': {
            'Meta': {'object_name': 'Volunteer'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'volunteered_at': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['volunteers.Event']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['volunteers']