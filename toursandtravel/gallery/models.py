from django.db import models
from django.db import models
from basemodel.models import BaseModel
from useraccounts.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from packages.models import *


# Create your models here.

class HolidaysPackagesGallery(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='gallery',null=True, blank=True)
    image = models.ImageField(upload_to='holidaypackagesgallery', blank=True, null=True)
    

    class Meta:
        ordering = ['id']
