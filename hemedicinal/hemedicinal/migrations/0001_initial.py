# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Ravimi nimi', max_length=255)),
                ('description', models.CharField(verbose_name='Ravimi kirjeldus', max_length=255)),
                ('price', models.FloatField(verbose_name='Ravimi hind')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Tootja nimi', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Ravimi nimi', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='drug',
            name='supplier',
            field=models.ForeignKey(verbose_name='Tarnija', to='hemedicinal.Supplier'),
            preserve_default=True,
        ),
    ]
