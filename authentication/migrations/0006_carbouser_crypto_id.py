# Generated by Django 5.0.4 on 2024-04-21 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_basetravel_id_alter_carbouser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='carbouser',
            name='crypto_id',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
