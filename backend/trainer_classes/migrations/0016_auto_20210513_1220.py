# Generated by Django 2.2.20 on 2021-05-13 12:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainer_classes", "0015_auto_20210507_1220"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trainerclass",
            name="attend_limit_count",
            field=models.PositiveIntegerField(
                default=0, validators=[django.core.validators.MaxValueValidator(250)]
            ),
        ),
    ]
