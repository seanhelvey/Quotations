# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'quotations_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
        ))
        db.send_create_signal(u'quotations', ['Author'])

        # Adding model 'Quote'
        db.create_table(u'quotations_quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('text', self.gf('django.db.models.fields.CharField')(default='', max_length=500)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quotations.Author'])),
        ))
        db.send_create_signal(u'quotations', ['Quote'])

        # Adding model 'Subject'
        db.create_table(u'quotations_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal(u'quotations', ['Subject'])

        # Adding M2M table for field quotation on 'Subject'
        m2m_table_name = db.shorten_name(u'quotations_subject_quotation')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subject', models.ForeignKey(orm[u'quotations.subject'], null=False)),
            ('quote', models.ForeignKey(orm[u'quotations.quote'], null=False))
        ))
        db.create_unique(m2m_table_name, ['subject_id', 'quote_id'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'quotations_author')

        # Deleting model 'Quote'
        db.delete_table(u'quotations_quote')

        # Deleting model 'Subject'
        db.delete_table(u'quotations_subject')

        # Removing M2M table for field quotation on 'Subject'
        db.delete_table(db.shorten_name(u'quotations_subject_quotation'))


    models = {
        u'quotations.author': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Author'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        u'quotations.quote': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Quote'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quotations.Author']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'})
        },
        u'quotations.subject': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Subject'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'quotation': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quotations.Quote']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['quotations']