# Generated by Django 5.0.4 on 2024-04-21 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_carbouser_dob_alter_basetravel_emission_saved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbouser',
            name='id',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]