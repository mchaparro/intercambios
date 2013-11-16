from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from intercambios.models import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView, CreateView

def crear_evento(request):
   
        
    return render_to_response('crear_evento.html', context_instance=RequestContext(request))
