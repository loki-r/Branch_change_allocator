# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_no', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('present_branch', models.CharField(max_length=30)),
                ('cpi', models.FloatField(max_length=30)),
                ('category', models.CharField(max_length=20, choices=[(b'GEN', b'GEN'), (b'OBC', b'OBC'), (b'SC', b'SC'), (b'ST', b'ST'), (b'PwD', b'PwD')])),
                ('pref_1', models.CharField(max_length=30)),
                ('pref_2', models.CharField(max_length=30)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
