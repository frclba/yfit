# Generated by Django 2.2.24 on 2021-06-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainer_classes", "0026_auto_20210602_0802"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainerclass",
            name="canceled",
            field=models.BooleanField(default=False),
        ),
    ]
