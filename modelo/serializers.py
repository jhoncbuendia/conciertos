from rest_framework.serializers import ModelSerializer
from modelo.models import Usuario , Artista, Perfil
from django.db import models

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        
        fields = ('id', 'nombre', 'password', 'correo', 'telefono')


class ArtistaSerializer(ModelSerializer):
    class Meta:
        model = Artista
        
        fields = ('id', 'nombre', 'genero')


class PerfilSerializer(ModelSerializer):
    class Meta:
        model = Perfil
        
        fields = ('id', 'usuario', 'ubicacion', 'artistas' )
       


    

    