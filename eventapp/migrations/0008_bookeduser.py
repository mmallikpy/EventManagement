# Generated by Django 5.1.2 on 2024-10-30 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "eventapp",
            "0007_alter_eventmodel_event_date_remove_eventmodel_user_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="BookedUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("book_status", models.BooleanField(default=False)),
                (
                    "event_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="eventapp.eventmodel",
                    ),
                ),
            ],
        ),
    ]
