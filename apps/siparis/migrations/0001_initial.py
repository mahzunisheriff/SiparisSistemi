# Generated by Django 4.2 on 2023-12-24 08:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adres', '0001_initial'),
        ('musteri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siparis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('toplam_fiyat', models.FloatField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 12, 24, 11, 28, 6, 493729), editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('adres', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adres.adres')),
                ('musteri', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='musteri.musteri')),
            ],
            options={
                'db_table': 'siparis',
            },
        ),
    ]