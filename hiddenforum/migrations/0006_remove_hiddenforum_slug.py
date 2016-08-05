# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hiddenforum', '0005_auto_20160805_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hiddenforum',
            name='slug',
        ),
    ]
