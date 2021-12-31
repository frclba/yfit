# Generated by Django 2.2.18 on 2021-02-02 11:01

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("taggit", "0003_taggeditem_add_unique_index"),
    ]

    operations = [
        migrations.CreateModel(
            name="TrainerClass",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("start_time", models.DateTimeField(blank=True, null=True)),
                ("duration", models.PositiveIntegerField()),
                (
                    "repeat",
                    models.CharField(
                        choices=[
                            ("never", "Never"),
                            ("daily", "Daily"),
                            ("weekly", "Weekly"),
                            ("monthly", "Monthly"),
                        ],
                        default="never",
                        max_length=10,
                    ),
                ),
                ("end_repeat", models.DateTimeField(blank=True, null=True)),
                (
                    "featured_photo",
                    models.ImageField(blank=True, null=True, upload_to="featured_photo"),
                ),
                ("details", models.TextField(blank=True, null=True)),
                ("equipment", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("in_person", "In Person"), ("virtual", "Virtual")],
                        default="in_person",
                        max_length=10,
                    ),
                ),
                (
                    "location",
                    django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
                ),
                (
                    "suggested_locations",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=django.contrib.postgres.fields.jsonb.JSONField(
                            null=True
                        ),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                ("location_notes", models.TextField(blank=True, null=True)),
                (
                    "safety_protocol",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("link", models.CharField(blank=True, max_length=255, null=True)),
                ("password", models.CharField(blank=True, max_length=128, null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                ("is_attendee_limit", models.BooleanField(default=False)),
                (
                    "attend_limit_count",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[django.core.validators.MaxValueValidator(100)],
                    ),
                ),
                ("promo_code", models.CharField(blank=True, max_length=8, null=True)),
                (
                    "cancellation_policy",
                    models.CharField(
                        choices=[
                            ("flexible", "Flexible"),
                            ("moderate", "Moderate"),
                            ("strict", "Strict"),
                        ],
                        default="flexible",
                        max_length=10,
                    ),
                ),
                ("hash", models.CharField(max_length=30, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("published_at", models.DateTimeField(blank=True, null=True)),
                (
                    "geotag",
                    django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trainer_classes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "verbose_name": "Trainer Class",
                "verbose_name_plural": "Trainer Classes",
                "db_table": "trainer_class",
            },
        ),
    ]
