# Generated by Django 4.1.1 on 2022-11-22 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amuseapp', '0009_alter_booking_count_child'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rides',
            name='description',
        ),
    ]
