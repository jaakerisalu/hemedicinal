# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150426_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tootaja',
            fields=[
                ('tootaja_kood', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'tootaja',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.AddField(
            model_name='user',
            name='tootaja',
            field=models.OneToOneField(to='accounts.Tootaja', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, unique=True, max_length=75),
            preserve_default=True,
        ),
    ]
