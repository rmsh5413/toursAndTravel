from django.db import models
from basemodel.models import *
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

# Create your models here.

class Homescreen(BaseModel):
    image=models.ImageField(upload_to="homescreen")
    title=models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Section'



class AboutUs(BaseModel):
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=200)
    description = RichTextField()
    image1 = models.ImageField(upload_to="AboutUs")
    image2 = models.ImageField(upload_to="About")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'
    

class AboutVisa(BaseModel):
    logo = models.ImageField(upload_to="AboutVisa")
    about= models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='about_visa')
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Mission | Vision'
        verbose_name_plural = 'Mission | Vision'

class VisaPoints(BaseModel):
    about_visa = models.ForeignKey(AboutVisa, on_delete=models.CASCADE, related_name='visa_points')
    point = models.CharField(max_length=700)
    
    def __str__(self):
        return self.point
    
    class Meta:
        verbose_name = 'List Mission | Vision'
        verbose_name_plural = 'List Mission | Vision'