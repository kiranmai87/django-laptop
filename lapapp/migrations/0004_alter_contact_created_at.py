# Generated by Django 4.2.2 on 2023-06-16 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "lapapp",
            "0003_rename_user_adduser_rename_passwoed_adduser_password_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 16, 21, 40, 4, 356022)
            ),
        ),
    ]