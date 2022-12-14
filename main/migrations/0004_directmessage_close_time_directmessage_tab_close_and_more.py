# Generated by Django 4.1.3 on 2022-12-01 12:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_directmessage_date_alter_groupmessage_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="directmessage",
            name="close_time",
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name="directmessage",
            name="tab_close",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="directmessage",
            name="wait_time",
            field=models.IntegerField(
                default=20,
                validators=[
                    django.core.validators.MaxValueValidator(100),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
        migrations.AddField(
            model_name="groupmessage",
            name="close_time",
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name="groupmessage",
            name="tab_close",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="groupmessage",
            name="wait_time",
            field=models.IntegerField(
                default=20,
                validators=[
                    django.core.validators.MaxValueValidator(100),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="directmessage",
            name="date",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="groupmessage",
            name="date",
            field=models.DateTimeField(null=True),
        ),
    ]
