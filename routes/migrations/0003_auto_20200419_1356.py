# Generated by Django 3.0.5 on 2020-04-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_auto_20200419_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='date_and_time',
            field=models.DateTimeField(null=True),
        ),
    ]
