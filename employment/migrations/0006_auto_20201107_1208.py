# Generated by Django 3.1.3 on 2020-11-07 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0005_auto_20201107_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='dateTime',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='is_registered',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='work',
        ),
    ]
