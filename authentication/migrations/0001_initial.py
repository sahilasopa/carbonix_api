# Generated by Django 5.0.4 on 2024-04-20 21:41

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTravel',
            fields=[
                ('start_time', models.DateTimeField(auto_created=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('emission_saved', models.DecimalField(decimal_places=2, max_digits=4)),
                ('distance', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('end_time', models.DateTimeField(null=True)),
                ('in_progress', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarboUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StationProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PrivateTravel',
            fields=[
                ('basetravel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authentication.basetravel')),
                ('start_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('start_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('end_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('end_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
            bases=('authentication.basetravel',),
        ),
        migrations.CreateModel(
            name='StationQRCode',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('qrcode', models.ImageField(upload_to='qr')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.stationprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='products')),
                ('price', models.DecimalField(decimal_places=6, max_digits=9)),
                ('categories', models.ManyToManyField(to='authentication.category')),
                ('tags', models.ManyToManyField(to='authentication.tags')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokens_accumulated', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('product', models.ManyToManyField(to='authentication.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.carbouser')),
            ],
        ),
        migrations.CreateModel(
            name='PublicTravel',
            fields=[
                ('basetravel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authentication.basetravel')),
                ('end_stop', models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='end_stop', to='authentication.stationprofile')),
                ('start_stop', models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='start_stop', to='authentication.stationprofile')),
            ],
            bases=('authentication.basetravel',),
        ),
    ]
