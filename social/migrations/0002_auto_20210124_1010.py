# Generated by Django 3.1.5 on 2021-01-24 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlike',
            name='like_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 24, 10, 10, 0, 638518)),
        ),
    ]
