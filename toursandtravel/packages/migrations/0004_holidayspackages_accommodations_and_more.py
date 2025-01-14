# Generated by Django 5.0.6 on 2024-09-05 10:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_packagesaccommodation_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='holidayspackages',
            name='accommodations',
            field=models.CharField(choices=[('Hotel', 'Hotel'), ('Resort', 'Resort'), ('Cottage', 'Cottage'), ('Villa', 'Villa'), ('Camp', 'Camp')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='holidayspackages',
            name='activity_duration',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='holidayspackages',
            name='destination',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='holidayspackages',
            name='duration',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='holidayspackages',
            name='end_point',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='holidayspackages',
            name='group_size',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='holidayspackages',
            name='max_altitude',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='holidayspackages',
            name='meals',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='holidayspackages',
            name='season',
            field=models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Autumn', 'Autumn'), ('Winter', 'Winter'), ('All', 'All')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='holidayspackages',
            name='start_point',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='holidayspackagescategory',
            name='equipment',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='holidayspackagescategory',
            name='description',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
