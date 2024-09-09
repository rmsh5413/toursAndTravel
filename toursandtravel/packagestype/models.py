from django.db import models

# Create your models here.
from django.db import models
from basemodel.models import BaseModel
from useraccounts.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator




class HolidaysPackagesType(BaseModel):
    name = models.CharField(max_length=255)
    ordering = models.PositiveBigIntegerField()
    slug = AutoSlugField(populate_from='name', unique=True,always_update=True)
    image = models.ImageField(upload_to='holidaypackagestype', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['ordering']



    # existing code
class HolidaysPackagesCategory(BaseModel):
    type = models.ForeignKey(HolidaysPackagesType, on_delete=models.CASCADE, related_name='categories', null=True, blank=True)
    name = models.CharField(max_length=255)
    ordering=models.PositiveBigIntegerField()
    slug = AutoSlugField(populate_from='name', unique=True,always_update=True)
    image = models.ImageField(upload_to='holidaypackagescategory', blank=True, null=True)
    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['ordering']

