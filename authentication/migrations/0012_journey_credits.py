# Generated by Django 5.0.4 on 2024-04-21 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_alter_journey_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='credits',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
    ]
