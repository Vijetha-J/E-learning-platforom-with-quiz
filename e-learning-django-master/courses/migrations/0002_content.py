# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django.db.models.deletion

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey( on_delete=django.db.models.deletion.CASCADE,to='contenttypes.ContentType')),
                ('module', models.ForeignKey(related_name='contents', on_delete=django.db.models.deletion.CASCADE, to='courses.Module')),
            ],
        ),
    ]
