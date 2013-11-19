from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.conf import settings
from intercambios.models import Evento
from django.contrib.auth import authenticate, login, logout
import datetime
import pytz

def crear_evento(request):
    if request.method == 'POST':
        local_TZ = pytz.timezone(settings.TIME_ZONE)
        
        nombre_evento = request.POST['nombre_evento']
        fecha = request.POST['fecha']
        participantes = request.POST['participantes']
        precio = request.POST['precio']
    
  
        fecha_evento = datetime.datetime.strptime(fecha, '%m/%d/%Y')
        fecha_evento_TZ = local_TZ.localize(fecha_evento)
        
        evento = Evento(admin=request.user, nombre=nombre_evento, precio=precio, numero_participantes=participantes, fecha_evento=fecha_evento_TZ)
        evento.save()
        
        data={
        'nuevo_evento':evento      
        }
        
        
        return render_to_response('evento_creado.html' , data , context_instance=RequestContext(request))
        
    return render_to_response('crear_evento.html', context_instance=RequestContext(request))
