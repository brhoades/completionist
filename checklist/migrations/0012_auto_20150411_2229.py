# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0011_auto_20150411_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='endDate',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
