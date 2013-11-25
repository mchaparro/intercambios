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
import random

def generar_intercambio(request, id):
    evento =  Evento.objects.get(id=id)
    print(dir(random))
    participantes = list(evento.participantes_evento.all())
    temporal = []
    for participante in participantes:
        tempo = list(evento.participantes_evento.all())
        tempo.remove(participante)
        
        #magia de python
        tempo = list(set([x for x in tempo if x not in temporal]))
        
        
        intercambio = random.choice(tempo)
        participante.intercambio = "%s - %s" % (intercambio.usuario.nombre,intercambio.usuario.id)
        participante.save()
        temporal.append(intercambio) 
        
        
    return HttpResponseRedirect('/detalles/evento/%s/' % evento.id) 
