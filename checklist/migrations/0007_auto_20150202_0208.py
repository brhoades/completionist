# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adminsortable.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0006_auto_20150202_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistentry',
            name='section',
            field=adminsortable.fields.SortableForeignKey(to='checklist.ChecklistSection'),
            preserve_default=True,
        ),
    ]
