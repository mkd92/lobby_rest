# Generated by Django 4.0.4 on 2022-06-01 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_alter_property_date_of_purchase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='user',
            new_name='user_id',
        ),
    ]
