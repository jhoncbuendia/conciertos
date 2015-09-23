from django.conf.urls import patterns, include, url
from django.contrib.redirects import models
from modelo.views import UsuarioList, UsuarioDetail, ArtistaList, ArtistaDetail, PerfilList, PerfilDetail, AgendaDetail
from modelo.views import ConciertoList, NoticiaDetail
    # Examples:
    # url(r'^$', 'wiiaccessapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    #urls OstApiK
urlpatterns = patterns('',
	
    url(r'^usuario/list/', UsuarioList),
    url(r'^usuario/detail/(?P<u>.+)/(?P<p>.+)/', UsuarioDetail),

    url(r'^artista/list/', ArtistaList),
    url(r'^artista/detail/(?P<pk>[0-9]+)/', ArtistaDetail),

    url(r'^perfil/list/', PerfilList),
    url(r'^perfil/detail/(?P<pk>.+)/', PerfilDetail),


    url(r'^concierto/list/$', ConciertoList.as_view()),
    url(r'^noticia/artista/(?P<id_artista>[0-9]+)/$', NoticiaDetail.as_view()),

    url(r'^agenda/detail/(?P<pk>[0-9]+)/$', AgendaDetail.as_view()),


    
)