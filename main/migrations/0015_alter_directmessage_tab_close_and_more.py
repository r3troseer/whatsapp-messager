# Generated by Django 4.1.3 on 2022-12-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0014_alter_directmessage_wait_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="directmessage",
            name="tab_close",
            field=models.BooleanField(
                choices=[(True, "Yes"), (False, "No")], default=False, null=True
            ),
        ),
        migrations.AlterField(
            model_name="groupmessage",
            name="tab_close",
            field=models.BooleanField(
                choices=[(True, "Yes"), (False, "No")], default=False, null=True
            ),
        ),
    ]
