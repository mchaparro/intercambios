from django.http import *
from django.db import connections
from django.contrib import messages
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext

class NombreMiddleware(object):
    
    def process_request(self, request):
       if request.user.is_anonymous():
           pass 
       elif request.path == '/perfil/usuario/':
           pass
       elif request.path == '/logout/':
           pass
       elif not request.user.nombre:
                messages.warning(request, '<h2 class="Diamond">Porfavor ingresa tu nombre completo para poder continuar</h2>')
                return render_to_response('perfil_usuario.html', {'next': request.path }, context_instance=RequestContext(request))
