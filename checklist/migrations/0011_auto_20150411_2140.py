# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0010_run_enddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='endDate',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
    ]
