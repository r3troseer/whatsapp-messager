# Generated by Django 4.1.3 on 2022-11-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="directmessage",
            name="date",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="groupmessage",
            name="date",
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]