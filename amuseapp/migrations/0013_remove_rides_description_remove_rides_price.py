# Generated by Django 4.1.2 on 2023-02-22 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amuseapp', '0012_merge_0003_initial_0011_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rides',
            name='description',
        ),
        migrations.RemoveField(
            model_name='rides',
            name='price',
        ),
    ]