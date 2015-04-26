# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=100, blank=True, null=True, verbose_name='Aadress'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, blank=True, null=True, verbose_name='Eesnimi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='id_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='Isikukood'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50, blank=True, null=True, verbose_name='Perekonnanimi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telefoni nr'),
            preserve_default=True,
        ),
    ]
