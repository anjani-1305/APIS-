# Generated by Django 4.2.3 on 2023-07-06 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='company',
            new_name='company_id',
        ),
    ]
