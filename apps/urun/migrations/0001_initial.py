# Generated by Django 4.2 on 2023-12-24 08:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urun',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ad', models.CharField(max_length=255)),
                ('aciklama', models.CharField(max_length=500)),
                ('fiyat', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 12, 24, 11, 28, 6, 493729), editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'urun',
            },
        ),
    ]
