# Generated by Django 4.2.1 on 2023-06-06 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='current_price',
            new_name='c',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='change',
            new_name='d',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='percent_change',
            new_name='dp',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='high_price',
            new_name='h',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='low_price',
            new_name='l',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='open_price',
            new_name='o',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='previous_close_price',
            new_name='pc',
        ),
    ]
