# Generated by Django 5.0.4 on 2024-04-21 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_remove_publictravel_basetravel_ptr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationprofile',
            name='latitude',
            field=models.DecimalField(decimal_places=8, max_digits=12),
        ),
        migrations.AlterField(
            model_name='stationprofile',
            name='longitude',
            field=models.DecimalField(decimal_places=8, max_digits=12),
        ),
    ]
