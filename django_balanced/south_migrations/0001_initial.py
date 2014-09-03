# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BankAccount'
        db.create_table(u'balanced_bank_accounts', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'bank_accounts', null=True, to=orm['roomchoice.CustomUser'])),
            ('account_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('routing_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('bank_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'django_balanced', ['BankAccount'])

        # Adding model 'Card'
        db.create_table(u'balanced_cards', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'cards', to=orm['roomchoice.CustomUser'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('expiration_month', self.gf('django.db.models.fields.IntegerField')()),
            ('expiration_year', self.gf('django.db.models.fields.IntegerField')()),
            ('last_four', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'django_balanced', ['Card'])

        # Adding model 'Credit'
        db.create_table(u'balanced_credits', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'credits', null=True, to=orm['roomchoice.CustomUser'])),
            ('bank_account', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'credits', to=orm['django_balanced.BankAccount'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'django_balanced', ['Credit'])

        # Adding model 'Debit'
        db.create_table(u'balanced_debits', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'debits', to=orm['roomchoice.CustomUser'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('card', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'debits', to=orm['django_balanced.Card'])),
        ))
        db.send_create_signal(u'django_balanced', ['Debit'])

        # Adding model 'Account'
        db.create_table(u'balanced_accounts', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'balanced_account', unique=True, to=orm['roomchoice.CustomUser'])),
        ))
        db.send_create_signal(u'django_balanced', ['Account'])


    def backwards(self, orm):
        # Deleting model 'BankAccount'
        db.delete_table(u'balanced_bank_accounts')

        # Deleting model 'Card'
        db.delete_table(u'balanced_cards')

        # Deleting model 'Credit'
        db.delete_table(u'balanced_credits')

        # Deleting model 'Debit'
        db.delete_table(u'balanced_debits')

        # Deleting model 'Account'
        db.delete_table(u'balanced_accounts')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'django_balanced.account': {
            'Meta': {'object_name': 'Account', 'db_table': "u'balanced_accounts'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'balanced_account'", 'unique': 'True', 'to': u"orm['roomchoice.CustomUser']"})
        },
        u'django_balanced.bankaccount': {
            'Meta': {'object_name': 'BankAccount', 'db_table': "u'balanced_bank_accounts'"},
            'account_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bank_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'routing_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'bank_accounts'", 'null': 'True', 'to': u"orm['roomchoice.CustomUser']"})
        },
        u'django_balanced.card': {
            'Meta': {'object_name': 'Card', 'db_table': "u'balanced_cards'"},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'expiration_month': ('django.db.models.fields.IntegerField', [], {}),
            'expiration_year': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_four': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cards'", 'to': u"orm['roomchoice.CustomUser']"})
        },
        u'django_balanced.credit': {
            'Meta': {'object_name': 'Credit', 'db_table': "u'balanced_credits'"},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'bank_account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'credits'", 'to': u"orm['django_balanced.BankAccount']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'credits'", 'null': 'True', 'to': u"orm['roomchoice.CustomUser']"})
        },
        u'django_balanced.debit': {
            'Meta': {'object_name': 'Debit', 'db_table': "u'balanced_debits'"},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'card': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'debits'", 'to': u"orm['django_balanced.Card']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'debits'", 'to': u"orm['roomchoice.CustomUser']"})
        },
        u'roomchoice.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "u'F'", 'max_length': '1'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite_id': ('uuidfield.fields.UUIDField', [], {'default': 'None', 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_validated': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "u'student'", 'max_length': '7'}),
            'unique_id': ('uuidfield.fields.UUIDField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        }
    }

    complete_apps = ['django_balanced']