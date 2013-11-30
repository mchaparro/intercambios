# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Usuario'
        db.create_table(u'intercambios_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, db_index=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(default=None, max_length=100, null=True, db_index=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('fecha_mod', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('intercambios', ['Usuario'])

        # Adding M2M table for field groups on 'Usuario'
        m2m_table_name = db.shorten_name(u'intercambios_usuario_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usuario', models.ForeignKey(orm['intercambios.usuario'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['usuario_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'Usuario'
        m2m_table_name = db.shorten_name(u'intercambios_usuario_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usuario', models.ForeignKey(orm['intercambios.usuario'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['usuario_id', 'permission_id'])

        # Adding model 'OpcionRegalo'
        db.create_table(u'intercambios_opcionregalo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('fecha_mod', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('opcion_de_regalo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(related_name='opcion_regalo', to=orm['intercambios.Usuario'])),
        ))
        db.send_create_signal('intercambios', ['OpcionRegalo'])

        # Adding model 'Evento'
        db.create_table(u'intercambios_evento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('fecha_evento', self.gf('django.db.models.fields.DateField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('numero_participantes', self.gf('django.db.models.fields.IntegerField')()),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('admin', self.gf('django.db.models.fields.related.ForeignKey')(related_name='eventos_admin', to=orm['intercambios.Usuario'])),
            ('estado', self.gf('django.db.models.fields.CharField')(default='activo', max_length=20)),
        ))
        db.send_create_signal('intercambios', ['Evento'])

        # Adding model 'ParticipantesEvento'
        db.create_table(u'intercambios_participantesevento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(related_name='participa_evento', to=orm['intercambios.Usuario'])),
            ('intercambio', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('evento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='participantes_evento', to=orm['intercambios.Evento'])),
        ))
        db.send_create_signal('intercambios', ['ParticipantesEvento'])

        # Adding unique constraint on 'ParticipantesEvento', fields ['usuario', 'evento']
        db.create_unique(u'intercambios_participantesevento', ['usuario_id', 'evento_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ParticipantesEvento', fields ['usuario', 'evento']
        db.delete_unique(u'intercambios_participantesevento', ['usuario_id', 'evento_id'])

        # Deleting model 'Usuario'
        db.delete_table(u'intercambios_usuario')

        # Removing M2M table for field groups on 'Usuario'
        db.delete_table(db.shorten_name(u'intercambios_usuario_groups'))

        # Removing M2M table for field user_permissions on 'Usuario'
        db.delete_table(db.shorten_name(u'intercambios_usuario_user_permissions'))

        # Deleting model 'OpcionRegalo'
        db.delete_table(u'intercambios_opcionregalo')

        # Deleting model 'Evento'
        db.delete_table(u'intercambios_evento')

        # Deleting model 'ParticipantesEvento'
        db.delete_table(u'intercambios_participantesevento')


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
        'intercambios.evento': {
            'Meta': {'object_name': 'Evento'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'eventos_admin'", 'to': "orm['intercambios.Usuario']"}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "'activo'", 'max_length': '20'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_evento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numero_participantes': ('django.db.models.fields.IntegerField', [], {}),
            'participantes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mis_eventos'", 'symmetrical': 'False', 'through': "orm['intercambios.ParticipantesEvento']", 'to': "orm['intercambios.Usuario']"}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        'intercambios.opcionregalo': {
            'Meta': {'object_name': 'OpcionRegalo'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion_de_regalo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opcion_regalo'", 'to': "orm['intercambios.Usuario']"})
        },
        'intercambios.participantesevento': {
            'Meta': {'unique_together': "(['usuario', 'evento'],)", 'object_name': 'ParticipantesEvento'},
            'evento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'participantes_evento'", 'to': "orm['intercambios.Evento']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intercambio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'participa_evento'", 'to': "orm['intercambios.Usuario']"})
        },
        'intercambios.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'email': ('django.db.models.fields.EmailField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['intercambios']