from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.conf import settings
from intercambios.models import Evento
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
import pytz
import json
from django.conf import settings


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
        
        data={
        'nuevo_evento':evento      
        }
        
        
        return render_to_response('detalles_evento.html' , data , context_instance=RequestContext(request))
        
    return render_to_response('crear_evento.html', context_instance=RequestContext(request))


@login_required
def detalles_evento(request, id):
    data={
          'nuevo_evento':Evento.objects.get(id=id)
          }
        
    return render_to_response('detalles_evento.html',data, context_instance=RequestContext(request))

@login_required
def mis_eventos(request):
    mis_eventos = Evento.objects.filter(admin = request.user)
    
    
    data={
        'mis_eventos':mis_eventos     
        }
    return render_to_response('index.html',data, context_instance=RequestContext(request))


