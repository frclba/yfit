# Generated by Django 2.2.15 on 2020-08-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_auto_20200827_1443"),
    ]

    operations = [
        migrations.AddField(
            model_name="paymentdetail",
            name="subscription_id",
            field=models.CharField(max_length=250, null=True),
        ),
    ]
