# Generated by Django 5.0.6 on 2024-09-06 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0009_alter_holidayspackagesgallery_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagesaccommodation',
            name='packages',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='packagesaccommodation', to='packages.holidayspackages'),
        ),
        migrations.AddField(
            model_name='packagesactivities',
            name='packages',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='packagesactivities', to='packages.holidayspackages'),
        ),
        migrations.AddField(
            model_name='packagesmeals',
            name='packages',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='packagesmeals', to='packages.holidayspackages'),
        ),
    ]
