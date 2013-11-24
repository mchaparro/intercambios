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

def random(request, id):
    evento =  Evento.objects.get(id=id)
    participantes = list(evento.participantes_evento.all())
    temporal = []
    for participante in participantes:
        tempo = participantes
        tempo.remove(participante)
        for temp in temporal:
            tempo.remove(temp)
        intercambio = random.choice(tempo)
        participante.intercambio = intercambio.usuario.nombre
        participante.save()
        temporal.append(intercambio) 
        
        
    return HttpResponseRedirect('/') 
