# -*- coding: utf-8 -*-
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from intercambios.models import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView, CreateView
from django.contrib import messages
from django.core.validators import validate_email

def login_user(request):
    try:
        next = request.GET['next']
    except:
        next = '/'
        
    logout(request)
    email = ''
    password = ''
    if request.POST:
        password = request.POST['password']
        email = request.POST['email']
        try:
            validate_email(email)
        except:
            messages.warning(request, '<h1 class="Diamond">El correo que indicaste no es valido</h1>')
            return HttpResponseRedirect('/')
        try:
                nombre = request.POST['nombre']
                password2 = request.POST['password2']
                if password != password2:
                    messages.warning(request, '<h1 class="Diamond">Las contraseñas no coinciden</h1>')
                    return HttpResponseRedirect('/')
                user = Usuario(nombre=nombre,username=email,email=email)
                user.set_password(password)
                user.save()
                user = authenticate(email=email, password=password)
                login(request,user)
                messages.success(request, '<h1 class="Diamond">%s!! Bienvenido al sistema de intercambios</h1>' % user.nombre)
                return HttpResponseRedirect('/')
                
        except:
            if not password or not email:
                messages.warning(request, '<h1 class="Diamond">Debes completar todos los campos</h1>')
                return HttpResponseRedirect('/')
            try:
                usuario = Usuario.objects.get(email=email)
            except:
                messages.warning(request, '<h1 class="Diamond">No existe ningun usuario registrado con ese correo</h1>')
                return HttpResponseRedirect('/')
            user = authenticate(email=email, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                return HttpResponseRedirect(next)
            else:
                messages.warning(request, '<h1 class="Diamond">Verifica tu contrase&ntilde;a</h1>')
        
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout_user(request):
  logout(request)
  return redirect(login_user)