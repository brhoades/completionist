# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChecklistEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('position', models.PositiveIntegerField(db_index=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('section', models.ForeignKey(to='checklist.ChecklistSection')),
            ],
            options={
                'ordering': ['position'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('checklist', models.ForeignKey(to='checklist.Checklist')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RunProgress',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('completed', models.DateTimeField(auto_now_add=True)),
                ('checked', models.BooleanField()),
                ('unsure', models.BooleanField()),
                ('entry', models.ForeignKey(to='checklist.ChecklistEntry')),
                ('run', models.ForeignKey(to='checklist.Run')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='checklistentries',
            name='section',
        ),
        migrations.DeleteModel(
            name='ChecklistEntries',
        ),
    ]
