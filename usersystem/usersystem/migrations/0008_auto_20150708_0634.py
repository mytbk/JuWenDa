# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersystem', '0007_auto_20150609_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='imei',
            field=models.TextField(blank=True, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='voteAnswers',
            field=models.ManyToManyField(blank=True, to='usersystem.Answer'),
            preserve_default=True,
        ),
    ]
