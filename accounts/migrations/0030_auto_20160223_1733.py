# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_auto_20160113_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='skill',
            field=models.TextField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='skill2',
            field=models.TextField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='skill3',
            field=models.TextField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='skill4',
            field=models.TextField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 23, 17, 33, 10, 864000, tzinfo=utc)),
        ),
    ]
