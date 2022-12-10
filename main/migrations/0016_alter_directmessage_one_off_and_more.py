# Generated by Django 4.1.3 on 2022-12-09 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0015_alter_directmessage_tab_close_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="directmessage",
            name="one_off",
            field=models.BooleanField(
                choices=[(True, "Yes"), (False, "No")], default=False
            ),
        ),
        migrations.AlterField(
            model_name="groupmessage",
            name="one_off",
            field=models.BooleanField(
                choices=[(True, "Yes"), (False, "No")], default=False
            ),
        ),
    ]