# Generated by Django 4.0.4 on 2022-04-18 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_alter_sensordata_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]