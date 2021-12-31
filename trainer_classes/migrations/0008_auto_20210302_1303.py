# Generated by Django 2.2.19 on 2021-03-02 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainer_classes", "0007_auto_20210301_1228"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="spot",
            options={},
        ),
        migrations.AddField(
            model_name="clientclasssignup",
            name="sms_delivered",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="clientclasssignup",
            name="sms_twilio_sid",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="spot",
            name="sms_delivered",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="spot",
            name="sms_twilio_sid",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]