# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0004_auto_20150202_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='image',
            field=models.ImageField(upload_to='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checklistentry',
            name='image',
            field=models.ImageField(upload_to='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checklistsection',
            name='image',
            field=models.ImageField(upload_to='', blank=True),
            preserve_default=True,
        ),
    ]
