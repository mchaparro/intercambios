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
    url(r'^$', login_required(TemplateView.as_view(template_name='index.html')), name="index"),
    (r'^login/$', login_user, {}, 'user_login'),
    (r'^logout/$', logout_user, {}, 'user_logout'),
    (r'^admin/', include(admin.site.urls)),
    #crear nuevo evento
    (r'^crear/evento/$', crear_evento, {}, 'crear_evento'),
    #agregar participante al evento
    (r'^evento/(?P<id>\d+)/agregar/participante/$', agregar_participante, {}, 'agregar_participante'),
    
)