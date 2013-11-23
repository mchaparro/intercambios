from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.conf import settings
from intercambios.models import Evento, ParticipantesEvento
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
import pytz

def agregar_participante(request, id):
    if request.method == 'POST':
        local_TZ = pytz.timezone(settings.TIME_ZONE)
        
        nombre_evento = request.POST['nombre_evento']
        fecha = request.POST['fecha']
        participantes = request.POST['participantes']
        precio = request.POST['precio']
        
        fecha_evento = datetime.datetime.strptime(fecha, '%m/%d/%Y')
        fecha_evento_TZ = local_TZ.localize(fecha_evento)
        
        evento = Evento(nombre=nombre_evento, precio=precio, participantes=participantes, fecha_evento=fecha_evento_TZ, admin=request.user)
        evento.save()
        
        data={
        'nuevo_evento':evento      
        }
        
        
        return render_to_response('evento_creado.html' , data , context_instance=RequestContext(request))
        
    return render_to_response('crear_evento.html', context_instance=RequestContext(request))


@login_required
def participar_evento(request,id):
    evento = Evento.objects.get(id=id)
    ParticipantesEvento.objects.get_or_create(usuario = request.user, evento = evento)
    messages.success(request, '<h1 class="Diamond">%s!! ahora ya eres parte del evento %s :)</h1>' % (request.user.nombre,evento.nombre))
    return HttpResponseRedirect('/detalles/evento/%s/' % evento.id)
