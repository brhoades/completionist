# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0005_auto_20150202_0028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checklistentry',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='checklistsection',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='checklistentry',
            name='order',
            field=models.PositiveIntegerField(editable=False, db_index=True, default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='checklistsection',
            name='order',
            field=models.PositiveIntegerField(editable=False, db_index=True, default=1),
            preserve_default=True,
        ),
    ]
