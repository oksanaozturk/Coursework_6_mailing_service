# Generated by Django 5.0.4 on 2024-06-13 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_remove_newsletter_time_finish_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newsletter",
            old_name="date_finish",
            new_name="datetime_finish",
        ),
        migrations.RenameField(
            model_name="newsletter",
            old_name="date_send",
            new_name="datetime_send",
        ),
        migrations.RenameField(
            model_name="newsletter",
            old_name="date_start",
            new_name="datetime_start",
        ),
    ]
