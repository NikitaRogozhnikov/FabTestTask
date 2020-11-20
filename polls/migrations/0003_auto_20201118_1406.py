# Generated by Django 2.2.10 on 2020-11-18 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20201118_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='ans_user',
        ),
        migrations.AlterField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 14, 6, 16, 969381)),
        ),
        migrations.AlterField(
            model_name='question',
            name='ques_type',
            field=models.CharField(choices=[('text', 't'), ('radio', 'r'), ('check', 'c')], default='t', max_length=4),
        ),
    ]
