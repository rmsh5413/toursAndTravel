# from django.db import models
# from basemodel.models import BaseModel
# from useraccounts.models import User
# from autoslug import AutoSlugField
# from ckeditor.fields import RichTextField
# from packages.models import *
# # Create your models here.


    
# class HolidaysPackagesItinerary(BaseModel):
#     package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='itinerary',null=True, blank=True)
#     ordering=models.PositiveBigIntegerField()
#     day = models.PositiveIntegerField()
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     image = models.ImageField(upload_to='holidaypackagesitinerary', blank=True, null=True)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         ordering = ['ordering']

