# Generated by Django 3.2.18 on 2023-03-30 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_auto_20230330_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateTimeField(default='2022-01-01 12:00:00'),
        ),
    ]