# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_auto_20150201_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runprogress',
            name='checked',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runprogress',
            name='unsure',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
