# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rssfeedfetcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedurl',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
