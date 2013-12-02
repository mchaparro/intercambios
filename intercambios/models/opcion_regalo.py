from django.db import models

class Regalo(models.Model):
    OPCIONES=(('Libros','Libros'),
    ('Chocolates','Chocolates'),
    ('Bebidas Alcoholicas','Bebidas Alcohoicas'),
    ('Ropa',' Ropa'),
    ('Accesorios',' Accesorios'),
    ('Perfumes',' Perfumes'),
    ('Electronica',' Electronica'),
    ('Otros',' Otros'),
    ('Categoria Libre',' Categoria Libre'))
    opcion_regalo = models.CharField(max_length = 50, choices = OPCIONES)
    
    def __unicode__(self):
        return "%s" % self.opcion_de_regalo
    
    class Meta:
        app_label = 'intercambios'
