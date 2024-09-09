from django.db import models
from basemodel.models import BaseModel
from useraccounts.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from packages.models import *

# Create your models here.
class HolidaysPackagesVideos(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='videos',null=True, blank=True)
    video = models.FileField(upload_to='holidaypackagesvideos', blank=True, null=True)
    

    class Meta:
        ordering = ['id']