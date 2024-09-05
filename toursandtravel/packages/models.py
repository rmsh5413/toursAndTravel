from django.db import models
from basemodel.models import BaseModel
from useraccounts.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
# Create your models here.

MEAL = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
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
    # existing code
class HolidaysPackagesCategory(BaseModel):
    name = models.CharField(max_length=255)
    ordering=models.PositiveBigIntegerField()
    slug = AutoSlugField(populate_from='name', unique=True)
    description = RichTextField()
    equipment = RichTextField()
    image = models.ImageField(upload_to='holidaypackagescategory', blank=True, null=True)
    
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
    destination = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    start_point=models.CharField(max_length=255)
    end_point=models.CharField(max_length=255)
    group_size=models.CharField(max_length=255)
    season=models.CharField(max_length=255, choices=SEASONS)
    meals = models.CharField(max_length=255, choices=MEAL)
    accommodations=models.CharField(max_length=255,choices=ACCOMMODATION)
    activity_duration=models.CharField(max_length=255)
    max_altitude=models.CharField(max_length=255)
    youtubeUrl=models.URLField(null=True, blank=True)

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
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['ordering']



class PackagesAccommodation(BaseModel):
    itinerary=models.ForeignKey(HolidaysPackagesItinerary, on_delete=models.CASCADE, related_name='accommodation',null=True, blank=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_at']

class PackagesMeals(BaseModel):
    itinerary=models.ForeignKey(HolidaysPackagesItinerary, on_delete=models.CASCADE, related_name='meals',null=True, blank=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_at']

class PackagesActivities(BaseModel):
    itinerary=models.ForeignKey(HolidaysPackagesItinerary, on_delete=models.CASCADE, related_name='activities',null=True, blank=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_at']
    


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
    ordering=models.PositiveBigIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    

    
    class Meta:
        ordering = ['ordering']


class HolidaysPackagesFaq(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='bookings',null=True, blank=True)
    ordering=models.PositiveBigIntegerField()
    question = models.CharField(max_length=255)
    answer = models.TextField()
    

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ['ordering']


class HolidaysPackagesComments(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',null=True, blank=True)
    comment = models.TextField()
    # review = models.PositiveIntegerField(validators =[MaxValueValidator(5)])
    

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-created_at']



class HolidaysPackagesHighlights(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='highlights',null=True, blank=True)
    ordering=models.PositiveBigIntegerField()
    detail = models.CharField(max_length=500)
    

    def __str__(self):
        return self.detail
    
    class Meta:
        ordering = ['ordering']



class HolidaysPackagesGallery(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='gallery',null=True, blank=True)
    ordering=models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='holidaypackagesgallery', blank=True, null=True)
    

    class Meta:
        ordering = ['ordering']


class HolidaysPackagesVideos(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='videos',null=True, blank=True)
    ordering=models.PositiveBigIntegerField()
    video = models.FileField(upload_to='holidaypackagesvideos', blank=True, null=True)
    

    class Meta:
        ordering = ['ordering']