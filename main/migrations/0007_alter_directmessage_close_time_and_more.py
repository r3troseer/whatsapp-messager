# Generated by Django 4.1.3 on 2022-12-02 20:24

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_alter_directmessage_wait_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="directmessage",
            name="close_time",
            field=models.IntegerField(default=3, null=True),
        ),
        migrations.AlterField(
            model_name="directmessage",
            name="date",
            field=models.DateTimeField(default=datetime.datetime.today, null=True),
        ),
        migrations.AlterField(
            model_name="directmessage",
            name="tab_close",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="directmessage",
            name="wait_time",
            field=models.IntegerField(
                default=20,
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(100),
                    django.core.validators.MinValueValidator(15),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="groupmessage",
            name="close_time",
            field=models.IntegerField(default=3, null=True),
        ),
        migrations.AlterField(
            model_name="groupmessage",
            name="date",
            field=models.DateTimeField(default=datetime.datetime.today, null=True),
        ),
        migrations.AlterField(
            model_name="groupmessage",
            name="tab_close",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="groupmessage",
            name="wait_time",
            field=models.IntegerField(
                default=20,
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(100),
                    django.core.validators.MinValueValidator(15),
                ],
            ),
        ),
    ]
