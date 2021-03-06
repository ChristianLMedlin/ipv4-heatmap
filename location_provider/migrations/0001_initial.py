# Generated by Django 3.1.4 on 2021-02-17 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(max_length=255)),
                ('geoname_id', models.CharField(max_length=255)),
                ('registered_country_geoname_id', models.CharField(max_length=255)),
                ('represented_country_geoname_id', models.CharField(max_length=255)),
                ('is_anonymous_proxy', models.BooleanField()),
                ('is_satellite_provider', models.BooleanField()),
                ('postal_code', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('accuracy_radius', models.IntegerField()),
            ],
        ),
    ]
