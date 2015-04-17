# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usersystem', '0003_usermodel_imei'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionUrl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('website', models.CharField(choices=[('csdn', 'CSDN')], max_length=5)),
                ('url', models.URLField()),
                ('question', models.ForeignKey(to='usersystem.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.CharField(choices=[('program', '编程'), ('math', '数学'), ('abroad', '出国')], blank=True, max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, default=None),
            preserve_default=False,
        ),
    ]
