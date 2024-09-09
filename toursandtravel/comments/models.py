from django.db import models
from basemodel.models import BaseModel
from useraccounts.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from packages.models import *
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class HolidaysPackagesComments(BaseModel):
    package = models.ForeignKey(HolidaysPackages, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',null=True, blank=True)
    comment = models.TextField()
    approve=models.BooleanField(default=False)
    rating = models.FloatField( validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    # review = models.PositiveIntegerField(validators =[MaxValueValidator(5)])
    

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-created_at']
