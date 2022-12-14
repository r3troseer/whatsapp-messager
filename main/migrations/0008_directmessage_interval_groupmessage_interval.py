# Generated by Django 4.1.3 on 2022-12-02 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_alter_directmessage_close_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="directmessage",
            name="interval",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1 hour", "One Hour"),
                    ("1 day", "One Day"),
                    ("7 days", "Seven Days"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="groupmessage",
            name="interval",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1 hour", "One Hour"),
                    ("1 day", "One Day"),
                    ("7 days", "Seven Days"),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]
