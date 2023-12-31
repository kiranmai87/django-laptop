# Generated by Django 4.2.2 on 2023-06-09 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=30)),
                ("message", models.CharField(max_length=60)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 6, 9, 18, 39, 13, 456880)
                    ),
                ),
                ("resolved_at", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=20)),
                ("passwoed", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=30)),
            ],
        ),
    ]
