# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=255)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profession', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 'Apteeker'), (2, 'Ravimihaldusjuht'), (3, 'Omanik')], default=1)),
                ('groups', models.ManyToManyField(related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_query_name='user', verbose_name='groups', blank=True, to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', help_text='Specific permissions for this user.', related_query_name='user', verbose_name='user permissions', blank=True, to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
