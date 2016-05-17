# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0003_auto_20160428_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, to='todolists.List'),
        ),
    ]
