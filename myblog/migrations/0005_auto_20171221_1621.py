# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20171221_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='place',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
