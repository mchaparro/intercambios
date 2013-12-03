from django.http import *
from django.db import connections
from django.contrib import messages

class NombreMiddleware(object):
    
    def process_request(self, request):
       if request.user.is_anonymous:
           pass 
       elif request.path == '/perfil/usuario/':
           pass
       elif not request.user.nombre:
                messages.warning(request, '<h2 class="Diamond">Porfavor ingresa tu nombre completo para poder continuar</h2>')
                return HttpResponseRedirect('/perfil/usuario/')