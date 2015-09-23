# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='foto',
            field=models.ImageField(upload_to=b'fotos'),
        ),
    ]
