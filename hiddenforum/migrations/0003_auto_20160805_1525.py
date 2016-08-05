# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hiddenforum', '0002_hiddenforum_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiddenforum',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
    ]
