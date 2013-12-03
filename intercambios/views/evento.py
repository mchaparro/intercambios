from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.conf import settings
from intercambios.models import Evento, ParticipantesEvento, Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pytz
import json
from django.conf import settings
import urllib
import datetime


def _json_object_hook(d): return namedtuple('object', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)


@login_required
def crear_evento(request):
    if request.method == 'POST':
        local_TZ = pytz.timezone(settings.TIME_ZONE)
        
        nombre_evento = request.POST['nombre_evento']
        fecha = request.POST['fecha']
        participantes = request.POST['participantes']
        
        if not int(participantes) > 1:
            messages.warning(request, '<h2 class="Diamond">El evento debe tener m&aacute;s de 1 participante</h2>')
            return HttpResponseRedirect('/') 
        
        precio = request.POST['precio']
        precio = precio.replace("$", "")
        precio = precio.replace(",", "")
        
        
        fecha_evento = datetime.datetime.strptime(fecha, '%m/%d/%Y').date()
        evento = Evento(admin=request.user, nombre=nombre_evento, precio=precio, numero_participantes=participantes, fecha_evento=fecha_evento)
        evento.save()
        
        ParticipantesEvento.objects.get_or_create(usuario = request.user, evento = evento)
        messages.success(request, '<h1 class="Diamond">%s!! ahora eres el administrador del evento <b>%s</b></br>debes mandar el link de tu evento a los dem&aacute;s participantes</h1>' % (request.user.nombre,evento.nombre))
        return HttpResponseRedirect('/detalles/evento/%s/' % evento.id)
        
    return render_to_response('crear_evento.html', context_instance=RequestContext(request))

@login_required
def perfil_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apodo = request.POST['apodo']
        if nombre:
            user = request.user
            user.nombre = ' '.join(nombre.split())
            user.apodo = ' '.join(apodo.split())
            user.save()
            messages.success(request, '<h1 class="Diamond">%s!! Se edito tu perfil con exito</h1>' % (request.user.nombre))
        return redirect('mis_eventos')
        
    return render_to_response('perfil_usuario.html', context_instance=RequestContext(request))


def format_fecha_delta(td):
    dias = abs(td.days)
    horas, remainder = divmod(td.seconds, 3600)
    minutos, segundos = divmod(remainder, 60)
    
    fecha_delta = {
      'dias' : "%02d" % dias,
      'horas' : "%02d" % horas,
      'minutos' : "%02d" % minutos,
      'segundos' : "%02d" % segundos
     
     }
    return fecha_delta

@login_required
def detalles_evento(request, id):
    try:
        evento = Evento.objects.get(id=id)
    except:
        messages.warning(request, '<h2 class="Diamond">No existe el evento seleccionado :(</h2>')
        return HttpResponseRedirect('/')
    participantes = evento.participantes.all()
    try:
        regala_a = ParticipantesEvento.objects.get(evento_id=id,usuario=request.user)
        regala_a = regala_a.intercambio
    except:
        messages.warning(request, '<h2 class="Diamond">No puedes acceder al evento: <b>"%s"</b> </br>es necesario solicitar una invitacion a %s</h2>' % (evento.nombre, evento.admin.nombre))
        return HttpResponseRedirect('/')
    
    fecha_evento = datetime.datetime.combine(evento.fecha_evento, datetime.time.min)
    fecha_delta = fecha_evento - datetime.datetime.today() 
    fecha_delta = format_fecha_delta(fecha_delta)
    
    data={
          'fecha_delta' : fecha_delta,
          'nuevo_evento':evento,
          'participantes':participantes,
          'participantes_faltantes':evento.numero_participantes-participantes.count(),
          'regala_a': regala_a
          }
        
    return render_to_response('detalles_evento.html',data, context_instance=RequestContext(request))

@login_required
def mis_eventos(request):
    mis_eventos = request.user.mis_eventos.all().filter(estado="activo")
                  
#     url = 'http://intercambios-node.herokuapp.com/eventos/usuario/%s/' % request.user.id
#     raw = urllib.urlopen(url)
#     mis_eventos = raw.readlines()
#     mis_eventos = json.loads(mis_eventos[0])
    
    data={
        'eventos_participa':list(mis_eventos)     
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
        
        if not int(participantes) > 1:
            messages.warning(request, '<h2 class="Diamond">El evento debe tener mas de 1 participante</h2>')
            return HttpResponseRedirect('/detalles/evento/%s/' % evento.id) 
        precio = request.POST['precio']
        precio = precio.replace("$", "")
        precio = precio.replace(",", "")
        
        fecha_evento = datetime.datetime.strptime(fecha, '%m/%d/%Y').date()
        evento.nombre=nombre_evento
        evento.precio=precio
        evento.numero_participantes=participantes
        evento.fecha_evento=fecha_evento
        evento.save()
        
        messages.warning(request, '<h2 class="Diamond">Se edito correctamente el evento %s</h2>' % evento.nombre)
        return HttpResponseRedirect('/detalles/evento/%s/' % evento.id) 
    data={
          'evento':evento,
          }
    return render_to_response('editar_evento.html',data, context_instance=RequestContext(request))


def cancelar_evento(request, id):
    evento = Evento.objects.get(id=id)
    messages.warning(request, '<h2 class="Diamond">El elimino el evento %s</h2>' % evento.nombre)
    evento.delete()
    return redirect('mis_eventos')

