# Generated by Django 2.2.20 on 2021-04-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainer_classes", "0011_trainerclass_free"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trainerclass",
            name="safety_protocol",
            field=models.TextField(blank=True, null=True),
        ),
    ]
