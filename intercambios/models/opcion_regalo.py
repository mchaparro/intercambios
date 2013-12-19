from django.db import models

class Regalo(models.Model):
    opcion_regalo = models.CharField(max_length = 50, unique=True)
    
    def __unicode__(self):
        return "%s" % self.opcion_de_regalo
    
    class Meta:
        app_label = 'intercambios'
