# -*- coding: utf-8 -*-
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from intercambios.models import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView, CreateView
from django.contrib import messages

def login_user(request):
    try:
        next = request.GET['next']
    except:
        next = '/'
        
    logout(request)
    email = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            nombre = request.POST['nombre']
            user = Usuario(nombre=nombre,username=username)
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.warning(request, '<h1 class="Diamond">%s!! bienvenido al sistema de intercambios navideños :)</br> para iniciar sesi&oacute deberas usar tu e-mail: %s </h1>' % (user.nombre,user.email))
            return HttpResponseRedirect(next)
        except:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                return HttpResponseRedirect(next)
        
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout_user(request):
  logout(request)
  return redirect(login_user)