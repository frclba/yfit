# Generated by Django 2.2.24 on 2021-09-09 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer_classes', '0037_mockmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mockapnsdevice',
            name='apnsdevice_ptr',
        ),
        migrations.DeleteModel(
            name='MockMessage',
        ),
        migrations.RemoveField(
            model_name='mockwebpushdevice',
            name='webpushdevice_ptr',
        ),
        migrations.DeleteModel(
            name='MockAPNSDevice',
        ),
        migrations.DeleteModel(
            name='MockWebPushDevice',
        ),
    ]
