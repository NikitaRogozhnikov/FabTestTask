# Generated by Django 2.2.10 on 2020-11-18 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20201118_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 18, 35, 31, 146498)),
        ),
        migrations.AlterField(
            model_name='question',
            name='ques_type',
            field=models.CharField(choices=[('text', 't'), ('radio', 'r'), ('check', 'c')], default='t', max_length=5),
        ),
    ]
