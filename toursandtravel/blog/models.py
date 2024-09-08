from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from basemodel.models import BaseModel

# Create your models here.

class Tag(BaseModel):
    name = models.CharField(max_length=100)
    slug=AutoSlugField(populate_from='name', unique=True, always_update=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag'
    

class Category(BaseModel):
    name = models.CharField(max_length=100)
    slug=AutoSlugField(populate_from='name', unique=True, always_update=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

class Blogs(BaseModel):
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to="Blogs", null=True, blank=True)
    logo = models.ImageField(upload_to="logoblg", null=True, blank=True)
    description = RichTextField()
    is_popular = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name='blogs', blank=True)
    tags = models.ManyToManyField(Tag, related_name='blogs', blank=True)

   

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'