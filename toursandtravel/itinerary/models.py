from django.db import models
from basemodel.models import BaseModel
from useraccounts.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from packages.models import *
# Create your models here.


    
class HolidaysPackagesItinerary(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='itinerary',null=True, blank=True)
    day = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='holidaypackagesitinerary', blank=True, null=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['day']



class PackagesAccommodation(BaseModel):
    packages=models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='packagesaccommodation',null=True, blank=True)
    itinerary=models.ForeignKey(HolidaysPackagesItinerary, on_delete=models.CASCADE, related_name='accommodation',null=True, blank=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_at']

class PackagesMeals(BaseModel):
    packages=models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='packagesmeals',null=True, blank=True)
    itinerary=models.ForeignKey(HolidaysPackagesItinerary, on_delete=models.CASCADE, related_name='meals',null=True, blank=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_at']

class PackagesActivities(BaseModel):
    packages=models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='packagesactivities',null=True, blank=True)
    itinerary=models.ForeignKey(HolidaysPackagesItinerary, on_delete=models.CASCADE, related_name='activities',null=True, blank=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_at']
    