# Generated by Django 4.2.2 on 2024-06-14 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_message_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'permissions': [('set_is_activated', 'Может менять активность рассылки')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]
