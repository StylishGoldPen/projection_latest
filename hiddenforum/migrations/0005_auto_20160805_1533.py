# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hiddenforum', '0004_auto_20160805_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiddenforum',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
