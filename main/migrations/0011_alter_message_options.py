# Generated by Django 4.2.2 on 2024-06-19 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_alter_newsletter_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="message",
            options={
                "permissions": [("set_update", "Может менять сообщения")],
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
            },
        ),
    ]