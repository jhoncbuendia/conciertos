from django.http.response import HttpResponse, Http404
from django.views.generic import View
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
import json
from modelo.serializers import UsuarioSerializer, ArtistaSerializer, PerfilSerializer
from modelo.models import Usuario, Artista, Perfil, Agenda, Concierto, Noticia
import hashlib
from django.utils.decorators import method_decorator


#-- servicio Usuario


class UsuarioList(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format = None):
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many = True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = UsuarioSerializer(data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioDetail(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, u, p):
        try:
        	usuario = Usuario.objects.get(nombre=u, password = hashlib.md5(p).hexdigest())
        	
        	return usuario
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, u, p, format=None):
        survey = self.get_object(u, p)
        
        print request.DATA
        serializer = UsuarioSerializer(survey, data = request.DATA)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, u, p, format=None):
        survey = self.get_object(u, p)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, u, p, format=None):
        survey = self.get_object(u, p)
        serializer = UsuarioSerializer(survey, data = request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



UsuarioList = UsuarioList.as_view()
UsuarioDetail  = UsuarioDetail.as_view()

#-- servicio Usuario




#-- servicio Artista

class ArtistaList(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format = None):
        artista = Artista.objects.all()
        serializer = ArtistaSerializer(artista, many = True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = ArtistaSerializer(data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtistaDetail(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Artista.objects.get(pk=pk)
        except Artista.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = ArtistaSerializer(survey, data = request.DATA)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = ArtistaSerializer(survey, data = request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



ArtistaList = ArtistaList.as_view()
ArtistaDetail  = ArtistaDetail.as_view()


#-- servicio Artista



#-- servicio Perfil

class PerfilList(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format = None):
        perfil = Perfil.objects.all()
        serializer = PerfilSerializer(perfil, many = True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = PerfilSerializer(data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerfilDetail(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Perfil.objects.get(usuario__nombre = pk)
        except Perfil.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = PerfilSerializer(survey, data = request.DATA)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = PerfilSerializer(survey, data = request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



PerfilList = PerfilList.as_view()
PerfilDetail  = PerfilDetail.as_view()


#-- servicio Perfil

class AgendaDetail(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AgendaDetail, self).dispatch(*args, **kwargs)

    def get(self, request, pk):

        
       
        return HttpResponse('down')

class ConciertoList(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ConciertoList, self).dispatch(*args, **kwargs)

    def get(self, request):
        c = Concierto.objects.all().order_by('-fecha')
        data = []
        concierto = {}
        concierto['nombre'] = c[0].nombre
        concierto['fecha'] = c[0].fecha.strftime("%Y:%D:%H:%M")
        concierto['artistas'] = []
        concierto['agendas'] = []
        concierto['momentos'] = []

        for a in  c[0].artistas.all():
            
            art = {}
            art['id'] = a.id
            art['nombre'] = a.nombre
            concierto['artistas'].append(art)

        for a in  c[0].agenda.all():
            ag = {}
            ag['id'] = a.id
            ag['artista'] = a.artista.nombre
            ag['fecha'] = a.fecha.strftime("%Y:%D:%H:%M")
            ag['titulo'] = a.titulo
            concierto['agendas'].append(ag)

        for m in  c[0].momentos.all():
            mom = {}
            mom['nombre'] = m.nombre
            mom['color'] = m.color
            mom['seccion'] = m.seccion.nombre
            concierto['momentos'].append(mom)


        data.append(concierto)
        return HttpResponse(json.dumps(data), content_type= "application/json")


class NoticiaDetail(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(NoticiaDetail, self).dispatch(*args, **kwargs)

    def get(self, request, id_artista):
        noticia = Noticia.objects.filter( artista__id = id_artista)
        data = []
        for n in noticia:
            
            notic = {}
            notic['titulo'] = n.titulo
            notic['subtitulo'] = n.subtitulo
            notic['detalle'] = n.detalle
            notic['fecha'] = n.fecha.strftime("%Y:%D:%H:%M")
            notic['foto'] = n.foto.url
            notic['artista'] = n.artista.nombre
            data.append(notic)
        return HttpResponse(json.dumps(data), content_type= "application/json")

        