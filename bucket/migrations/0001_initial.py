# Generated by Django 2.1.2 on 2018-10-21 06:01

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('ws84_x', models.FloatField()),
                ('ws84_y', models.FloatField()),
                ('address', models.TextField()),
                ('note', models.TextField()),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
                ('point', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
            ],
        ),
    ]