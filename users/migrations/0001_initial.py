# Generated by Django 3.0.5 on 2020-04-10 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField()),
                ('type', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddIndex(
            model_name='serviceuser',
            index=models.Index(fields=['first_name'], name='users_servi_first_n_fbd499_idx'),
        ),
    ]
