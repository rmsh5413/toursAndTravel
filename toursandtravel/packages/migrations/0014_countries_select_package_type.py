# Generated by Django 5.0.6 on 2024-09-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0013_cities_countries_holidayspackages_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='countries',
            name='select_package_type',
            field=models.CharField(choices=[('International', 'International'), ('Domestic', 'Domestic')], default='International', max_length=255),
        ),
    ]