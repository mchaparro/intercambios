from django.db import models

class Evento(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_evento = models.DateTimeField()
    nombre = models.CharField(max_length=50)
    participantes = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    admin = models.ForeignKey('Usuario', related_name='eventos')
    
    def __unicode__(self):
        return "%s" % self.nombre
    
    class Meta:
        app_label = 'intercambios'
