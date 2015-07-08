# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Standard'
        db.create_table(u'search_standard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'search', ['Standard'])

        # Adding model 'Issue'
        db.create_table(u'search_issue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vol', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('no', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'search', ['Issue'])

        # Adding model 'Activity'
        db.create_table(u'search_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['search.Issue'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('goals', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'search', ['Activity'])

        # Adding M2M table for field standards on 'Activity'
        m2m_table_name = db.shorten_name(u'search_activity_standards')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'search.activity'], null=False)),
            ('standard', models.ForeignKey(orm[u'search.standard'], null=False))
        ))
        db.create_unique(m2m_table_name, ['activity_id', 'standard_id'])


    def backwards(self, orm):
        # Deleting model 'Standard'
        db.delete_table(u'search_standard')

        # Deleting model 'Issue'
        db.delete_table(u'search_issue')

        # Deleting model 'Activity'
        db.delete_table(u'search_activity')

        # Removing M2M table for field standards on 'Activity'
        db.delete_table(db.shorten_name(u'search_activity_standards'))


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