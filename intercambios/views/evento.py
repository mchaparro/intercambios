from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from intercambios.models import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView, CreateView

def crear_evento(request):
    if request.method == 'POST':
        
        nombre_evento = request.POST['nombre_evento']
        fecha = request.POST['fecha']
        participantes = request.POST['participantes']
        precio = request.POST['precio']
        
        evento = Evento(nombre=nombre_evento, precio=precio, participantes=participantes, fecha_evento=fecha, admin=request.user)
        evento.save()
        
        return render_to_response('index.html', context_instance=RequestContext(request))
        
    return render_to_response('crear_evento.html', context_instance=RequestContext(request))
