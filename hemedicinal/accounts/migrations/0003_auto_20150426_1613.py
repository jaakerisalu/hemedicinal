# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150426_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_code',
            field=models.IntegerField(verbose_name='Isikukood'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(verbose_name='Telefoni nr'),
            preserve_default=True,
        ),
    ]
