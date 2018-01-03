# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_testmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testmodel',
            old_name='logincode',
            new_name='place',
        ),
        migrations.AddField(
            model_name='testmodel',
            name='contact',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
