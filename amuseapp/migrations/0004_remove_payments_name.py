# Generated by Django 4.1.1 on 2023-02-28 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amuseapp', '0003_payments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='name',
        ),
    ]
