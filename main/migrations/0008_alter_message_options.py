# Generated by Django 4.2.2 on 2024-06-14 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_alter_client_owner_alter_message_author"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="message",
            options={
                "permissions": [
                    ("set_is_activated", "Может менять активность рассылки")
                ],
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
            },
        ),
    ]
