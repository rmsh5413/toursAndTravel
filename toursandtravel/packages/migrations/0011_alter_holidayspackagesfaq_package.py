# Generated by Django 5.0.6 on 2024-09-06 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0010_packagesaccommodation_packages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidayspackagesfaq',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='packages.holidayspackages'),
        ),
    ]
