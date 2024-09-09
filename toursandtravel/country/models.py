from django.db import models

# Create your models here.
from django.db import models
from basemodel.models import BaseModel
from useraccounts.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from packagestype.models import HolidaysPackagesType, HolidaysPackagesCategory

# Create your models here.

INTERNATIONALORDOMESTIC = (
    ('International', 'International'),
    ('Domestic', 'Domestic')
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
