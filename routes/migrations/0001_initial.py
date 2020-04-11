# Generated by Django 3.0.5 on 2020-04-10 11:33

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time', models.DateTimeField(default=None)),
                ('start_point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('finish_point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ServiceUser')),
            ],
        ),
        migrations.AddIndex(
            model_name='route',
            index=models.Index(fields=['user', 'date_and_time', 'start_point'], name='routes_rout_user_id_3a95b2_idx'),
        ),
    ]
