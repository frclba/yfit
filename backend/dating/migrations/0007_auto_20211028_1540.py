# Generated by Django 2.2.24 on 2021-10-28 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_message_inbox'),
        ('dating', '0006_delete_setting'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Inbox',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
