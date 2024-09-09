from django.db import models
from basemodel.models import BaseModel
from useraccounts.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from packagestype.models import HolidaysPackagesType, HolidaysPackagesCategory

# Create your models here.

MEAL = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('All', 'All')
)
INTERNATIONALORDOMESTIC = (
    ('International', 'International'),
    ('Domestic', 'Domestic')
)

SEASONS = (
    ('Spring', 'Spring'),
    ('Summer', 'Summer'),
    ('Autumn', 'Autumn'),
    ('Winter', 'Winter'),
    ('All', 'All'),
)

ACCOMMODATION = (
    ('Hotel', 'Hotel'),
    ('Resort', 'Resort'),
    ('Cottage', 'Cottage'),
    ('Villa', 'Villa'),
    ('Camp', 'Camp'),
)






class Countries(BaseModel):
    CONTINENTS = (
            ('Africa', 'Africa'),
            ('Asia', 'Asia'),
            ('Europe', 'Europe'),
            ('North America', 'North America'),
            ('South America', 'South America'),
            ('Oceania', 'Oceania'),
            ('Antarctica', 'Antarctica')
        )
    
    select_package_type=models.CharField(max_length=255, choices=INTERNATIONALORDOMESTIC,default='International')
    continent = models.CharField(max_length=255, choices=CONTINENTS)
    name = models.CharField(max_length=255)
    ordering = models.PositiveBigIntegerField()
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)
    image = models.ImageField(upload_to='countries', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['ordering']



class Cities(BaseModel):
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, related_name='cities',null=  True, blank=True)
    name = models.CharField(max_length=255)
    ordering=models.PositiveBigIntegerField()
    slug = AutoSlugField(populate_from='name', unique=True,always_update=True)
    image = models.ImageField(upload_to='cities', blank=True, null=True)
    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['ordering']

class HolidaysPackages(BaseModel):
    country=models.ForeignKey(Countries, on_delete=models.CASCADE, related_name='countrypackages',null=  True, blank=True)
    city=models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='citypackages',null=  True, blank=True)
    packagetype = models.ForeignKey(HolidaysPackagesType, on_delete=models.CASCADE, related_name='packagecategories',null=  True, blank=True)
    category = models.ForeignKey(HolidaysPackagesCategory, on_delete=models.CASCADE, related_name='packages',null=  True, blank=True)
    ordering=models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True,always_update=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='holidaypackages', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    destination = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    start_point=models.CharField(max_length=255)
    end_point=models.CharField(max_length=255)
    group_size=models.CharField(max_length=255)
    season=models.CharField(max_length=255, choices=SEASONS)
    meals = models.CharField(max_length=255, choices=MEAL)
    select_package_type=models.CharField(max_length=255, choices=INTERNATIONALORDOMESTIC)
    accommodations=models.CharField(max_length=255,choices=ACCOMMODATION)
    activity_duration=models.CharField(max_length=255)
    max_altitude=models.CharField(max_length=255)
    youtubeUrl=models.URLField(null=True, blank=True)
    mapUrl=models.URLField(max_length=1000,null=True, blank=True)
    pdfManual=models.FileField(upload_to='holidaypackagespdf', blank=True, null=True)
    description = RichTextField()
    equipment = RichTextField()
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['ordering']



class HolidaysPackagesInclusion(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='inclusions',null=True, blank=True)
    ordering=models.PositiveBigIntegerField()
    detail = models.CharField(max_length=505)
    

    def __str__(self):
        return self.detail
    
    class Meta:
        ordering = ['ordering']


class HolidaysPackagesExclusion(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='exclusions',null=True, blank=True)
    ordering=models.PositiveBigIntegerField()
    detail = models.CharField(max_length=505)
    

    def __str__(self):
        return self.detail

    
    class Meta:
        ordering = ['ordering']



class HolidaysPackagesNotice(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='notices',null=True, blank=True)
    ordering=models.PositiveBigIntegerField()
    title=models.CharField(max_length=255)
    description = RichTextField()
    

    def __str__(self):
        return self.title

    
    class Meta:
        ordering = ['ordering']


class HolidaysPackagesDates(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='dates',null=True, blank=True) 
    start_date = models.DateField()
    end_date = models.DateField()
    

    
    class Meta:
        ordering = ['start_date']


class HolidaysPackagesFaq(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='faqs',null=True, blank=True)
    ordering=models.PositiveBigIntegerField()
    question = models.CharField(max_length=255)
    answer = models.TextField()
    

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ['ordering']





class HolidaysPackagesHighlights(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='highlights',null=True, blank=True)
    ordering=models.PositiveBigIntegerField()
    detail = models.CharField(max_length=500)
    

    def __str__(self):
        return self.detail
    
    class Meta:
        ordering = ['ordering']




