from django.db import models
from basemodel.models import BaseModel
from useraccounts.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['ordering']

    
class HolidaysPackagesItinerary(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='itinerary',null=True, blank=True)
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


class HolidaysPackagesInclusion(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='inclusions',null=True, blank=True)
    ordering=models.PositiveBigIntegerField()
    detail = models.CharField(max_length=505)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.detail
    
    class Meta:
        ordering = ['ordering']


class HolidaysPackagesExclusion(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='exclusions',null=True, blank=True)
    ordering=models.PositiveBigIntegerField()
    detail = models.CharField(max_length=505)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.detail

    
    class Meta:
        ordering = ['ordering']



class HolidaysPackagesNotice(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='notices',null=True, blank=True)
    ordering=models.PositiveBigIntegerField()
    title=models.CharField(max_length=255)
    description = RichTextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    
    class Meta:
        ordering = ['ordering']


class HolidaysPackagesDates(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='dates',null=True, blank=True) 
    ordering=models.PositiveBigIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    
    class Meta:
        ordering = ['ordering']


class HolidaysPackagesFaq(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='bookings',null=True, blank=True)
    ordering=models.PositiveBigIntegerField()
    question = models.CharField(max_length=255)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ['ordering']


class HolidaysPackagesComments(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',null=True, blank=True)
    comment = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-created_at']