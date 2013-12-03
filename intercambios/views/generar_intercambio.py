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
import json
import random

def generar_intercambio(request, id):
    evento =  Evento.objects.get(id=id)
    sorteado = ParticipantesEvento.objects.filter(evento__id = id)[0]
    if not (evento.admin == request.user):
        messages.warning(request, '<h2 class="Diamong">Solo el creador del evento puede generar el intercambio %s</h2>' % evento.nombre)
        return HttpResponse('{"error":"Solo el creador del evento puede generar el intercambio"}', content_type='application/json');
    if not (evento.numero_participantes == evento.participantes.all().count()):
        messages.warning(request, '<h2 class="Diamong">No se puede generar el intercambio hasta que esten registrados todos los participantes</h2>')
        return HttpResponse('{"error":"No se puede generar el intercambio hasta que esten registrados todos los participantes"}', content_type='application/json');
    if (sorteado.intercambio):
        messages.warning(request, '<h2 class="Diamong">El sorteo ya fue realizado, no puedes cambiar tu destino</h2>')
        return HttpResponse('{"error":"El sorteo ya fue realizado, no puedes cambiar tu destino"}', content_type='application/json');
      
    participantes = list(evento.participantes_evento.all())
    temporal = []
    for participante in participantes:
        tempo = list(evento.participantes_evento.all())
        tempo.remove(participante)
        
        #magia de python
        tempo = list(set([x for x in tempo if x not in temporal]))
        
        
        intercambio = random.choice(tempo)
        participante.intercambio = "%s" % (intercambio.usuario.nombre)
        participante.save()
        temporal.append(intercambio) 
        
        
    return HttpResponse('{}', content_type='application/json');
