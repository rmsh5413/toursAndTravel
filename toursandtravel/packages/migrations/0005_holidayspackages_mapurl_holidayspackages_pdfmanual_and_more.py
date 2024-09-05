# Generated by Django 5.0.6 on 2024-09-05 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_holidayspackages_accommodations_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='holidayspackages',
            name='mapUrl',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='holidayspackages',
            name='pdfManual',
            field=models.FileField(blank=True, null=True, upload_to='holidaypackagespdf'),
        ),
        migrations.AddField(
            model_name='holidayspackages',
            name='youtubeUrl',
            field=models.URLField(blank=True, null=True),
        ),
    ]