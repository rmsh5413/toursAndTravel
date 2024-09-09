# Generated by Django 5.0.6 on 2024-09-09 05:12

import autoslug.fields
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('select_package_type', models.CharField(choices=[('International', 'International'), ('Domestic', 'Domestic')], default='International', max_length=255)),
                ('continent', models.CharField(choices=[('Africa', 'Africa'), ('Asia', 'Asia'), ('Europe', 'Europe'), ('North America', 'North America'), ('South America', 'South America'), ('Oceania', 'Oceania'), ('Antarctica', 'Antarctica')], max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('ordering', models.PositiveBigIntegerField()),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='countries')),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('ordering', models.PositiveBigIntegerField()),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cities')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='country.countries')),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
    ]