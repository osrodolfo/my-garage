# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0002_registro_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='imagenes'),
        ),
    ]
