# Generated by Django 4.2.1 on 2023-06-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField()),
                ('current_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('change', models.DecimalField(decimal_places=4, max_digits=10)),
                ('percent_change', models.DecimalField(decimal_places=4, max_digits=10)),
                ('high_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('low_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('open_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('previous_close_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('t', models.BigIntegerField()),
            ],
        ),
    ]
