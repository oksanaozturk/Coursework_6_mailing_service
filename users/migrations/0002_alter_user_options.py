# Generated by Django 4.2.2 on 2024-06-14 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('set_is_active', 'Может блокировать пользователя')], 'verbose_name': 'Пользоаптель', 'verbose_name_plural': 'Пользователи'},
        ),
    ]