# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('titulo', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('genero', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Concierto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('fecha', models.DateTimeField()),
                ('agenda', models.ManyToManyField(to='modelo.Agenda', blank=True)),
                ('artistas', models.ManyToManyField(to='modelo.Artista', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Momento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('color', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50, blank=True)),
                ('subtitulo', models.CharField(max_length=50, blank=True)),
                ('detalle', models.TextField(max_length=50, null=True, blank=True)),
                ('fecha', models.DateTimeField()),
                ('foto', models.CharField(max_length=50, blank=True)),
                ('artista', models.ForeignKey(blank=True, to='modelo.Artista', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ubicacion', models.IntegerField(null=True, blank=True)),
                ('artistas', models.ManyToManyField(to='modelo.Artista', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=50, blank=True)),
                ('password', models.CharField(max_length=50, blank=True)),
                ('correo', models.CharField(max_length=50, null=True, blank=True)),
                ('telefono', models.TextField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(blank=True, to='modelo.Usuario'),
        ),
        migrations.AddField(
            model_name='momento',
            name='seccion',
            field=models.ForeignKey(blank=True, to='modelo.Seccion', null=True),
        ),
        migrations.AddField(
            model_name='concierto',
            name='momentos',
            field=models.ManyToManyField(to='modelo.Momento', blank=True),
        ),
        migrations.AddField(
            model_name='agenda',
            name='artista',
            field=models.ForeignKey(blank=True, to='modelo.Artista', null=True),
        ),
    ]
