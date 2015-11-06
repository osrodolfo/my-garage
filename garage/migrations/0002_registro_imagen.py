# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='imagen',
            field=models.ImageField(upload_to='static', blank=True),
        ),
    ]
