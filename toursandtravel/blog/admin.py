from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Blogs)
admin.site.register(Category)
admin.site.register(Tag)