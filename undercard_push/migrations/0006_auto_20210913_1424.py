# Generated by Django 2.2.24 on 2021-09-13 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainer_classes', '0038_auto_20210909_1948'),
        ('undercard_push', '0005_clientclasssignuppushlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preclassclientpushlog',
            name='client',
        ),
        migrations.AddField(
            model_name='preclassclientpushlog',
            name='client_class_signup',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='trainer_classes.ClientClassSignUp'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ClientClassSignupPushLog',
        ),
    ]
