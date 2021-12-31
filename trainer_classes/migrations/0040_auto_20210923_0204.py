# Generated by Django 2.2.24 on 2021-09-23 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0015_edit_solarschedule_events_choices'),
        ('trainer_classes', '0039_clientclasssignup_trainer_notified'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientclasssignup',
            name='payout_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payout_signup', to='django_celery_beat.PeriodicTask'),
        ),
    ]
