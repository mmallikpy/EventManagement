# Generated by Django 5.1.2 on 2024-11-01 14:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("eventapp", "0010_eventcatorogy_eventmodel_catevent"),
    ]

    operations = [
        migrations.RenameField(
            model_name="eventmodel",
            old_name="catevent",
            new_name="category",
        ),
    ]
