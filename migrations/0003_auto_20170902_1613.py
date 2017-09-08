# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-02 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20170901_1225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-end_date']},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.Language'),
        ),
    ]