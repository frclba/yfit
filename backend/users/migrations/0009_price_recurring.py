# Generated by Django 2.2.15 on 2020-09-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_auto_20200827_2011"),
    ]

    operations = [
        migrations.AddField(
            model_name="price",
            name="recurring",
            field=models.BooleanField(default=False),
        ),
    ]
