# Generated by Django 4.0.4 on 2022-11-20 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_lightdata_brightness'),
    ]

    operations = [
        migrations.CreateModel(
            name='myTodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addedDate', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('dueDate', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
