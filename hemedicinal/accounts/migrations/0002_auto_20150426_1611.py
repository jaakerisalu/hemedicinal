# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=100, default='Sütiste 54-15', verbose_name='Aadress'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, default='Jaak', verbose_name='Eesnimi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='id_code',
            field=models.SmallIntegerField(default=3940, verbose_name='Isikukood'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50, default='Erisalu', verbose_name='Perekonnanimi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.SmallIntegerField(default=562, verbose_name='Telefoni nr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Aktiivne'), (2, 'Puhkusel'), (3, 'Mitteaktiivne')], null=True, default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='emaili aadress'),
            preserve_default=True,
        ),
    ]
