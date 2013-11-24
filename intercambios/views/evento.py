from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.conf import settings
from intercambios.models import Evento, ParticipantesEvento, Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
import pytz
import json
from django.conf import settings
import urllib


def _json_object_hook(d): return namedtuple('object', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)


@login_required
def crear_evento(request):
    if request.method == 'POST':
        local_TZ = pytz.timezone(settings.TIME_ZONE)
        
        nombre_evento = request.POST['nombre_evento']
        fecha = request.POST['fecha']
        participantes = request.POST['participantes']
        precio = request.POST['precio']
        precio = precio.replace("$", "")
        
        
        fecha_evento = datetime.datetime.strptime(fecha, '%m/%d/%Y').date()
        evento = Evento(admin=request.user, nombre=nombre_evento, precio=precio, numero_participantes=participantes, fecha_evento=fecha_evento)
        evento.save()
        
        ParticipantesEvento.objects.get_or_create(usuario = request.user, evento = evento)
        messages.success(request, '<h1 class="Diamond">%s!! ahora eres el administrador del evento %s :)</br>debes mandar el link de tu evento a los dem&aacute;s participantes</h1>' % (request.user.nombre,evento.nombre))
        return HttpResponseRedirect('/detalles/evento/%s/' % evento.id)
        
    return render_to_response('crear_evento.html', context_instance=RequestContext(request))


@login_required
def detalles_evento(request, id):
    evento = Evento.objects.get(id=id)
    participantes = evento.participantes.all()
    
    data={
          'nuevo_evento':evento,
          'participantes':participantes,
          'participantes_faltantes':evento.numero_participantes-participantes.count()
          }
        
    return render_to_response('detalles_evento.html',data, context_instance=RequestContext(request))

@login_required
def mis_eventos(request):
    eventos_participa = request.user.eventos.all()
                  
#     url = 'http://localhost:1212/get/eventos/usuario/%s/' % request.user.id
#     raw = urllib.urlopen(url)
#     mis_eventos = raw.readlines()
#     mis_eventos = json.loads(mis_eventos[0])
    
    data={
        'eventos_participa':eventos_participa     
        }
    return render_to_response('index.html',data, context_instance=RequestContext(request))
    
@login_required
def editar_evento(request, id):
    evento = Evento.objects.get(id=id)
    if not evento.admin == request.user:
         return HttpResponseRedirect('/')
    if request.method == 'POST':
        local_TZ = pytz.timezone(settings.TIME_ZONE)
        
        nombre_evento = request.POST['nombre_evento']
        fecha = request.POST['fecha']
        participantes = request.POST['participantes']
        precio = request.POST['precio']
        precio = precio.replace("$", "")
        
        fecha_evento = datetime.datetime.strptime(fecha, '%m/%d/%Y').date()
        evento.nombre=nombre_evento
        evento.precio=precio
        evento.numero_participantes=participantes
        evento.fecha_evento=fecha_evento
        evento.save()
        
        messages.warning(request, '<h2 class="Diamong">Se edito correctamente el evento %s</h2>' % evento.nombre)
        return HttpResponseRedirect('/')
    data={
          'evento':evento,
          }
        
    return render_to_response('editar_evento.html',data, context_instance=RequestContext(request))
def cancelar_evento(request):
    return render_to_response('editar_evento.html',data, context_instance=RequestContext(request))

