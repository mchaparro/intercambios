from django.db import models

class Evento(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_evento = models.DateField()
    nombre = models.CharField(max_length=50)
    numero_participantes = models.IntegerField()
    participantes = models.ManyToManyField('Usuario',through='ParticipantesEvento', related_name='mis_eventos')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    admin = models.ForeignKey('Usuario', related_name='eventos_admin')
    estado = models.CharField(max_length = 20, choices = (('activo', 'activo'),('cancelado',' cancelado')), default='activo')
    
    def __unicode__(self):
        return "%s" % self.nombre
    
    class Meta:
        app_label = 'intercambios'

class InvitacionesPendientes(models.Model):
    usuario = models.ForeignKey('Usuario', related_name='invitaciones_pendientes')
    evento = models.ForeignKey('Evento', related_name='invitaciones_pendientes')
    estado = models.CharField(max_length = 20, choices = (('pendiente', 'pendiente'),('cancelado',' cancelado'),('aceptado',' aceptado')), default='pendiente')
    
    def __unicode__(self):
        return "%s" % self.id
    
    class Meta:
        unique_together = ['usuario','evento']
        app_label = 'intercambios'
                
class ParticipantesEvento(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey('Usuario', related_name='participa_evento')
    intercambio = models.CharField(max_length=100, blank=True, null=True)
    evento = models.ForeignKey('Evento', related_name='participantes_evento')
    regalos = models.ManyToManyField('Regalo',through='RegalosParticipante', related_name='participantes_evento')
    detalle_regalo = models.CharField(max_length=200, blank=True, null=True, default='')
    
   
    def __unicode__(self):
        return "%s" % self.id
    
    class Meta:
        app_label = 'intercambios'
        unique_together = ['usuario','evento']
        
class RegalosParticipante(models.Model):
    participante = models.ForeignKey('ParticipantesEvento', related_name='regalos_participante')
    regalo = models.ForeignKey('Regalo')
   
    
    def __unicode__(self):
        return "%s" % self.id
    
    class Meta:
        app_label = 'intercambios'
