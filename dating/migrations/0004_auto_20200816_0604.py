# Generated by Django 2.2.15 on 2020-08-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dating", "0003_auto_20200816_0603"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userphoto",
            name="photo",
            field=models.URLField(null=True),
        ),
    ]
