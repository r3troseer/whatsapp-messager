# Generated by Django 4.1.3 on 2022-12-01 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_directmessage_close_time_directmessage_tab_close_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="directmessage",
            name="date",
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name="groupmessage",
            name="date",
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
