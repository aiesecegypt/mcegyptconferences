# Generated by Django 2.2.28 on 2025-03-31 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('momentum25', '0002_delegate_agree_policy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delegate',
            old_name='phone',
            new_name='phone_number',
        ),
    ]
