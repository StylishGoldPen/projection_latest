# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hiddenforum', '0003_auto_20160805_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiddenforum',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
