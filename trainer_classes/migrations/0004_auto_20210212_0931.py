# Generated by Django 2.2.18 on 2021-02-12 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainer_classes", "0003_auto_20210205_1949"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trainerclass",
            name="featured_photo",
            field=models.ImageField(
                blank=True, max_length=200, null=True, upload_to="featured_photo"
            ),
        ),
    ]
