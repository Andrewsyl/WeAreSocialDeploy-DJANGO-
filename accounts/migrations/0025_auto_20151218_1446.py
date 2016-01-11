# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20151211_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 14, 46, 33, 576000, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
