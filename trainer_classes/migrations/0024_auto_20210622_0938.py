# Generated by Django 2.2.24 on 2021-06-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainer_classes", "0023_auto_20210615_1038"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainerclass",
            name="featured_video",
            field=models.FileField(blank=True, null=True, upload_to="featured_video"),
        )
    ]