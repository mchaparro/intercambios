# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone

class UsuariosManager(BaseUserManager):
    def create_user(self, username, email="",password="", nombre=""):
        """
        Creates and saves user with the given username and password.
        """
        if not username:
            raise ValueError('Favor de proporcionar un nombre de usuario valido')

        usuario = self.model(
            email=UserManager.normalize_email(email),username=username,nombre=nombre
        )
        
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, username="",email="",password="",nombre=""):
        """
        Creates and saves a superuser with the given username
        """
        usuario = self.create_user(username=username, email=email,nombre=nombre,password=password)
        usuario.is_superuser = True
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50,db_index=True,unique=True)
    apodo = models.CharField(max_length=100,blank=True,null=True,default="")
    email = models.EmailField(max_length=100, blank=True,null=True,default=None,db_index=True)
    nombre = models.CharField(max_length=100)
    
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UsuariosManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre']
    

    def __unicode__(self):
        if (self.apodo):
            return self.apodo
        else:
            return "%s" % (' '.join(self.nombre.split()[0:2]))

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin
    
    class Meta:
        app_label = 'intercambios'
