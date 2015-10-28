# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('docfile', models.FileField(upload_to='csv_files')),
            ],
        ),
        migrations.AlterField(
            model_name='info',
            name='category',
            field=models.CharField(choices=[('GEN', 'GEN'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'), ('PwD', 'PwD')], max_length=20),
        ),
    ]
