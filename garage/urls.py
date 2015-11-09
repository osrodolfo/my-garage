from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.Listar),
    url(r'^dato/(?P<pk>[0-9]+)/$', views.Detalles),
    url(r'^dato/new/$', views.Nuevo, name='Nuevo'),
    url(r'^dato/(?P<pk>[0-9]+)/edit/$', views.Editar, name='Editar'),
]
