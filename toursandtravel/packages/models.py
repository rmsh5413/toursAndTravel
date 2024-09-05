from django.db import models
from basemodel.models import BaseModel
from useraccounts.models import User
from autoslug import AutoSlugField

# Create your models here.


class HolidaysPackagesCategory(BaseModel):
    name = models.CharField(max_length=255)
    ordering=models.PositiveBigIntegerField()
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='holidaypackagescategory', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['ordering']


class HolidaysPackages(BaseModel):
    category = models.ForeignKey(HolidaysPackagesCategory, on_delete=models.CASCADE, related_name='packages')
    ordering=models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='holidaypackages', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['ordering']

    
class HolidaysPackagesItinerary(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='itinerary')
    ordering=models.PositiveBigIntegerField()
    day = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='holidaypackagesitinerary', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['ordering']
