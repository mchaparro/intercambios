from django.db import models

class OpcionRegalo(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)
    opcion_de_regalo = models.CharField(max_length=100)
    usuario = models.ForeignKey('Usuario', related_name='opcion_regalo')
    
    
    def __unicode__(self):
        return "%s" % self.opcion_de_regalo
    
    class Meta:
        app_label = 'intercambios'
