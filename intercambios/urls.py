from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView
from views import *
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
      
    (r'^$',mis_eventos ,{} , 'mis_eventos'),
    #url(r'^$', login_required(TemplateView.as_view(template_name='index.html')), name="index"),
    (r'^login/$', login_user, {}, 'user_login'),
    (r'^logout/$', logout_user, {}, 'user_logout'),
    (r'^admin/', include(admin.site.urls)),
    #modificar perfil
    (r'^perfil/usuario/$', perfil_usuario, {}, 'perfil_usuario'),
    #enviar invitacion
    (r'^invitacion/evento/(?P<id>\d+)/$', enviar_invitacion, {}, 'enviar_invitacion'),
    #editar evento
    (r'^editar/evento/(?P<id>\d+)/$', editar_evento, {}, 'editar_evento'),
    #crear evento
    (r'^crear/evento/$', crear_evento, {}, 'crear_evento'),
    #cancelar evento
    (r'^cancelar/evento/(?P<id>\d+)/$', cancelar_evento, {}, 'cancelar_evento'),
    #agregar participante al evento
    (r'^participar/evento/(?P<id>\d+)/$', participar_evento, {}, 'participar_evento'),
    #detalles evento
    (r'^detalles/evento/(?P<id>\d+)/$', detalles_evento, {}, 'detalles_evento'),
    #pop-invitar participantes
    (r'^invitar/evento/(?P<id>\d+)/$', invitar_evento, {}, 'invitar_evento'),
    #pop-elegir regalo
    (r'^elegir/regalo/(?P<id>\d+)/$', elegir_regalo, {}, 'elegir_regalo'),
    #random
    (r'^generar/intercambio/evento/(?P<id>\d+)/$', generar_intercambio, {}, 'generar_intercambio'),
    url(r'', include('social_auth.urls')),
    
)