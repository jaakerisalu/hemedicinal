# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hemedicinal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Substance',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Mõjuaine nimi')),
                ('description', models.CharField(max_length=100, verbose_name='Mõjuaine kirjelus')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='drug',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1, verbose_name='Töötaja', related_name='created_drugs'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drug',
            name='manufacturer',
            field=models.ForeignKey(default=1, verbose_name='Tootja', to='hemedicinal.Manufacturer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drug',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, choices=[(1, 'Aktiivne'), (2, 'Mitteaktiivne')], verbose_name='Seisund'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drug',
            name='substance',
            field=models.ForeignKey(default=1, verbose_name='Mõjuaine', to='hemedicinal.Substance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='description',
            field=models.CharField(max_length=100, default='Kange', verbose_name='Tootja kirjelus'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='address',
            field=models.CharField(max_length=100, default='Kuudi 6', verbose_name='Tarnija Aadress'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='email',
            field=models.CharField(max_length=100, default='supply@firm.ee', verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='phone',
            field=models.SmallIntegerField(default=562, verbose_name='Telefoni nr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, choices=[(1, 'Aktiivne'), (2, 'Mitteaktiivne')], verbose_name='Seisund'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='drug',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Ravimi nimi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='drug',
            name='price',
            field=models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ravimi hind'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Tootja nimi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Tarnija nimi'),
            preserve_default=True,
        ),
    ]
