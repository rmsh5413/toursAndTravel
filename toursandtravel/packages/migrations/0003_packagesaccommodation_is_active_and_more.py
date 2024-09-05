# Generated by Django 5.0.6 on 2024-09-05 10:29

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_packagesaccommodation_packagesactivities_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagesaccommodation',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='packagesactivities',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='packagesmeals',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='HolidaysPackagesGallery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ordering', models.PositiveBigIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='holidaypackagesgallery')),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='packages.holidayspackages')),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='HolidaysPackagesVideos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ordering', models.PositiveBigIntegerField()),
                ('video', models.FileField(blank=True, null=True, upload_to='holidaypackagesvideos')),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='packages.holidayspackages')),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
    ]