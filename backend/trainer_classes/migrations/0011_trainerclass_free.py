# Generated by Django 2.2.19 on 2021-04-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainer_classes", "0010_auto_20210316_1234"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainerclass",
            name="free",
            field=models.BooleanField(default=False),
        ),
    ]
