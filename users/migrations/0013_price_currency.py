# Generated by Django 2.2.16 on 2020-12-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0012_price_cancelled"),
    ]

    operations = [
        migrations.AddField(
            model_name="price",
            name="currency",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
