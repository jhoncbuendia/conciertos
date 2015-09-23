from django.db import models
import hashlib
# Create your models here.

class Usuario(models.Model):
	nombre = models.CharField(max_length=50, blank = True , unique=True)
	password = models.CharField(max_length=50, blank = True)
	correo = models.CharField(max_length=50,  blank = True, null = True)
	telefono = models.TextField(max_length=50,  blank = True, null = True)

	def save(self, *args, **kwargs):
		self.password = hashlib.md5(self.password).hexdigest()
		super(Usuario, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre


class Artista(models.Model):
	nombre = models.CharField(max_length=50, blank = True)
	genero = models.CharField(max_length=50,  blank = True, null = True)

	def __unicode__(self):
		return self.nombre



class Perfil(models.Model):
	usuario  = models.OneToOneField('Usuario', blank = True)
	ubicacion = models.IntegerField(  blank = True, null = True)
	artistas = models.ManyToManyField('Artista',  blank = True)

	def __unicode__(self):
		return str(self.usuario)	

class Noticia(models.Model):
	titulo = models.CharField(max_length=50, blank = True)
	subtitulo =  models.CharField(max_length=50, blank = True)
	detalle = models.TextField(max_length=50,  blank = True, null = True)
	fecha = models.DateTimeField() 
	foto = models.ImageField(upload_to='fotos')
	artista = models.ForeignKey('Artista', blank = True, null = True)

	def __unicode__(self):
		return str(self.titulo)

class Seccion(models.Model):
	nombre = models.CharField(max_length=50, blank = True)
	

	def __unicode__(self):
		return str(self.nombre)

class Concierto(models.Model):
	nombre = models.CharField(max_length=50, blank = True)
	fecha = models.DateTimeField() 
	artistas = models.ManyToManyField('Artista', blank = True)
	momentos = models.ManyToManyField('Momento',  blank = True)
	agenda = models.ManyToManyField('Agenda',  blank = True)
	def __unicode__(self):
		return str(self.nombre)

class Momento(models.Model):
	nombre = models.CharField(max_length=50, blank = True)
	color = models.CharField(max_length=50, blank = True)
	seccion = models.ForeignKey('Seccion', blank = True, null = True)

	def __unicode__(self):
		return str(self.nombre)

class Agenda(models.Model):
	artista = models.ForeignKey('Artista', blank = True,  null = True)
	fecha = models.DateTimeField() 
	titulo = models.CharField(max_length=50, blank = True)

	def __unicode__(self):
		return str(self.titulo)