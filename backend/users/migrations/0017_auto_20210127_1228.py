# Generated by Django 2.2.16 on 2021-01-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0016_auto_20201217_1041"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="workout_types",
            field=models.ManyToManyField(blank=True, to="users.WorkoutType"),
        ),
    ]