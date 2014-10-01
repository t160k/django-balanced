# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

# For django custom user model see:
# http://kevindias.com/writing/django-custom-user-models-south-and-reusable-apps/

# Safe User import for Django < 1.5
try:
    from django.contrib.auth import get_user_model
except ImportError:
    from django.contrib.auth.models import User
else:
    User = get_user_model()

# With the default User model these will be 'auth.User' and 'auth.user'
# so instead of using orm['auth.User'] we can use orm[user_orm_label]
user_orm_label = '%s.%s' % (User._meta.app_label, User._meta.object_name)
user_model_label = '%s.%s' % (User._meta.app_label, User._meta.module_name)

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BankAccount'
        db.create_table(u'balanced_bank_accounts', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'bank_accounts', null=True, to=orm[user_orm_label])),
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
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'cards', to=orm['accounts.T160KUser'])),
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
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'credits', null=True, to=orm['accounts.T160KUser'])),
            ('bank_account', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'credits', to=orm['django_balanced.BankAccount'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('statement_descriptor', self.gf('django.db.models.fields.CharField')(max_length=12, null=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'django_balanced', ['Credit'])

        # Adding model 'Debit'
        db.create_table(u'balanced_debits', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'debits', to=orm['accounts.T160KUser'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('statement_descriptor', self.gf('django.db.models.fields.CharField')(max_length=12, null=True)),
            ('card', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'debits', null=True, to=orm['django_balanced.Card'])),
            ('bank_account', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'debits', null=True, to=orm['django_balanced.BankAccount'])),
        ))
        db.send_create_signal(u'django_balanced', ['Debit'])

        # Adding model 'Account'
        db.create_table(u'balanced_accounts', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'balanced_account', unique=True, to=orm['accounts.T160KUser'])),
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
        # We've accounted for changes to:
        # the app name, table name, pk attribute name, pk column name.
        # The only assumption left is that the pk is an AutoField (see below)
        user_model_label: {
            'Meta': {
                'object_name': User.__name__,
                'db_table': "'%s'" % User._meta.db_table
            },
            User._meta.pk.attname: (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True',
                'db_column': "'%s'" % User._meta.pk.column}
            ),
        },
        u'django_balanced.account': {
            'Meta': {'object_name': 'Account', 'db_table': "u'balanced_accounts'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'balanced_account'", 'unique': 'True', 'to': u"orm['accounts.T160KUser']"})
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'bank_accounts'", 'null': 'True', 'to': u"orm['accounts.T160KUser']"})
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cards'", 'to': u"orm['accounts.T160KUser']"})
        },
        u'django_balanced.credit': {
            'Meta': {'object_name': 'Credit', 'db_table': "u'balanced_credits'"},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'bank_account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'credits'", 'to': u"orm['django_balanced.BankAccount']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'statement_descriptor': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'credits'", 'null': 'True', 'to': u"orm['accounts.T160KUser']"})
        },
        u'django_balanced.debit': {
            'Meta': {'object_name': 'Debit', 'db_table': "u'balanced_debits'"},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'bank_account': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'debits'", 'null': 'True', 'to': u"orm['django_balanced.BankAccount']"}),
            'card': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'debits'", 'null': 'True', 'to': u"orm['django_balanced.Card']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'statement_descriptor': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'debits'", 'to': u"orm['accounts.T160KUser']"})
        }
    }

    complete_apps = ['django_balanced']