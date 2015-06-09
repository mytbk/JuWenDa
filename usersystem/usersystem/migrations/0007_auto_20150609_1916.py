# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersystem', '0006_auto_20150511_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('link', models.URLField()),
                ('good', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='voteAnswers',
            field=models.ManyToManyField(to='usersystem.Answer'),
            preserve_default=True,
        ),
    ]
