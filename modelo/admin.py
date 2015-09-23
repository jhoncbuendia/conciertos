from django.contrib import admin
from django.contrib.auth.models import User
from modelo.models import Usuario, Artista, Perfil, Noticia, Seccion, Concierto
from modelo.models import Momento, Agenda
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Artista)
admin.site.register(Perfil)
admin.site.register(Noticia)
admin.site.register(Seccion)
admin.site.register(Concierto)
admin.site.register(Momento)
admin.site.register(Agenda)


