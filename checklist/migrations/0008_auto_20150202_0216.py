# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0007_auto_20150202_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistentry',
            name='section',
            field=models.ForeignKey(to='checklist.ChecklistSection'),
            preserve_default=True,
        ),
    ]
