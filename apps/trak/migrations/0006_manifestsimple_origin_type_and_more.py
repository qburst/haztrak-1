# Generated by Django 4.0.4 on 2022-04-18 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trak', '0005_manifestsimple_submission_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manifestsimple',
            name='origin_type',
            field=models.CharField(choices=[('Web', 'Web'), ('Service', 'Service'), ('Mail', 'Mail')], default='Service', max_length=25),
        ),
        migrations.AlterField(
            model_name='manifestsimple',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 18, 10, 8, 17, 988842), null=True),
        ),
    ]