# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=200)),
                ('modelo', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('vendido', models.BooleanField()),
                ('precio', models.DecimalField(max_digits=10, decimal_places=2)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('marca', models.ForeignKey(to='garage.Marca')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
