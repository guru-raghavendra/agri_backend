# Generated by Django 4.2.8 on 2023-12-12 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExpiringToken',
        ),
    ]
