from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.conf import settings
from intercambios.models import Evento, ParticipantesEvento, Usuario, InvitacionesPendientes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
import json
import pytz

def _json_object_hook(d): return namedtuple('object', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

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
    participantes_max = evento.numero_participantes
    participantes_actuales = evento.participantes.all().count()
    try:
        invitacion = InvitacionesPendientes.objects.get(usuario=request.user,evento=evento)
        invitacion.delete()
    except:
        pass
    if request.user in evento.participantes.all():
        messages.info(request, '<h1 class="Diamond">%s!! tu ya formas parte del evento %s </h1>' % (request.user,evento.nombre))
        return HttpResponseRedirect('/detalles/evento/%s/' % evento.id)
    disponibles = participantes_max-participantes_actuales
    if(disponibles>0):
        ParticipantesEvento.objects.get_or_create(usuario = request.user, evento = evento)
        messages.success(request, '<h1 class="Diamond">%s!! ahora ya eres parte del evento %s </h1>' % (request.user,evento.nombre))
        return HttpResponseRedirect('/detalles/evento/%s/' % evento.id)
    else:
        messages.error(request, '<h1 class="Diamond">%s!! El numero maximo de participantes del evento ha llegado a su limite </h1>' % (request.user.nombre))
        return HttpResponseRedirect('/' )
        
@login_required
def invitar_evento(request,id):
    evento = Evento.objects.get(id=id)
    ParticipantesEvento.objects.get_or_create(usuario = request.user, evento = evento)
    usuarios = Usuario.objects.exclude(id__in = evento.participantes.all().values_list('id', flat=True))
    data={
    'evento':evento,
    'usuarios':usuarios    
    }
    return render_to_response('invitar_evento.html' , data , context_instance=RequestContext(request))


def elegir_regalo(request,id):
    evento = Evento.objects.get(id=id)
    ParticipantesEvento.objects.get_or_create(usuario = request.user, evento = evento)
    
    data={
    'evento':evento    
    }
    return render_to_response('elegir_regalo.html' , data , context_instance=RequestContext(request))


def enviar_invitacion(request,id):
    evento = Evento.objects.get(id=id)
    try:
        ids_usuarios_invitar = json2obj(request.POST['usuarios'])
        
        for id_usuario in ids_usuarios_invitar:
            usuario = Usuario.objects.get(id=id_usuario)
            if not usuario in evento.participantes.all():
                invitacion = InvitacionesPendientes.objects.get_or_create(usuario=usuario,evento=evento)
                invitacion = InvitacionesPendientes.objects.get(usuario=usuario,evento=evento)
                invitacion.estado = 'pendiente'
                invitacion.save()
        
    except:
        pass
    return HttpResponse('{}', content_type='application/json')