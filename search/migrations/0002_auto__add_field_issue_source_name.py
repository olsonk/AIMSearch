# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Issue.source_name'
        db.add_column(u'search_issue', 'source_name',
                      self.gf('django.db.models.fields.CharField')(default='AIMS Magazine', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Issue.source_name'
        db.delete_column(u'search_issue', 'source_name')


    models = {
        u'search.activity': {
            'Meta': {'object_name': 'Activity'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'goals': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['search.Issue']"}),
            'standards': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['search.Standard']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'search.issue': {
            'Meta': {'object_name': 'Issue'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'source_name': ('django.db.models.fields.CharField', [], {'default': "'AIMS Magazine'", 'max_length': '30'}),
            'vol': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'search.standard': {
            'Meta': {'object_name': 'Standard'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['search']