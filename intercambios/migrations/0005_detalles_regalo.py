# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ParticipantesEvento.detalles'
        db.delete_column(u'intercambios_participantesevento', 'detalles')

        # Adding field 'ParticipantesEvento.detalle_regalo'
        db.add_column(u'intercambios_participantesevento', 'detalle_regalo',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ParticipantesEvento.detalles'
        db.add_column(u'intercambios_participantesevento', 'detalles',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'ParticipantesEvento.detalle_regalo'
        db.delete_column(u'intercambios_participantesevento', 'detalle_regalo')


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
        'intercambios.invitacionespendientes': {
            'Meta': {'unique_together': "(['usuario', 'evento'],)", 'object_name': 'InvitacionesPendientes'},
            'estado': ('django.db.models.fields.CharField', [], {'default': "'pendiente'", 'max_length': '20'}),
            'evento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invitaciones_pendientes'", 'to': "orm['intercambios.Evento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invitaciones_pendientes'", 'to': "orm['intercambios.Usuario']"})
        },
        'intercambios.participantesevento': {
            'Meta': {'unique_together': "(['usuario', 'evento'],)", 'object_name': 'ParticipantesEvento'},
            'detalle_regalo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'evento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'participantes_evento'", 'to': "orm['intercambios.Evento']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intercambio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'regalos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'participantes_evento'", 'symmetrical': 'False', 'through': "orm['intercambios.RegalosParticipante']", 'to': "orm['intercambios.Regalo']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'participa_evento'", 'to': "orm['intercambios.Usuario']"})
        },
        'intercambios.regalo': {
            'Meta': {'object_name': 'Regalo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion_regalo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'intercambios.regalosparticipante': {
            'Meta': {'object_name': 'RegalosParticipante'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participante': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'regalos_participante'", 'to': "orm['intercambios.ParticipantesEvento']"}),
            'regalo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['intercambios.Regalo']"})
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