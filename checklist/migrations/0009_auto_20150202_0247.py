# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0008_auto_20150202_0216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklistentry',
            name='position',
        ),
        migrations.RemoveField(
            model_name='checklistsection',
            name='position',
        ),
    ]
