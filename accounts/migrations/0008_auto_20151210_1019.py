# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20151210_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='subsciption_end',
        ),
        migrations.AddField(
            model_name='user',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 10, 10, 19, 57, 508000, tzinfo=utc)),
        ),
    ]
