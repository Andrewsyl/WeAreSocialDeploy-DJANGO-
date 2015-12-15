# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_subsciption_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subsciption_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 10, 10, 17, 40, 914000, tzinfo=utc)),
        ),
    ]
