# Generated by Django 3.2.18 on 2023-03-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='allergens',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
