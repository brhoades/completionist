# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0009_auto_20150202_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='endDate',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
    ]
