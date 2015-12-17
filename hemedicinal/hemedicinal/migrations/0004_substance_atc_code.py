# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hemedicinal', '0003_auto_20150426_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='substance',
            name='atc_code',
            field=models.CharField(default='kartul', max_length=7, verbose_name='ATC kood'),
            preserve_default=False,
        ),
    ]
