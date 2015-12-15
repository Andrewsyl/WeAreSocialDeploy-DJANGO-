# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20151211_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hometown',
            field=models.CharField(default=datetime.datetime(2015, 12, 11, 14, 54, 43, 25000, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 11, 14, 48, 31, 476000, tzinfo=utc)),
        ),
    ]
