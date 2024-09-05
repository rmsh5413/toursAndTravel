from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(HolidaysPackagesCategory)

class PackagesAccommodationInline(admin.TabularInline):
    model = PackagesAccommodation
    extra = 1  # Number of extra forms to display

class PackagesMealsInline(admin.TabularInline):
    model = PackagesMeals
    extra = 1

class PackagesActivitiesInline(admin.TabularInline):
    model = PackagesActivities
    extra = 1

@admin.register(HolidaysPackagesItinerary)
class HolidaysPackagesItineraryAdmin(admin.ModelAdmin):
    inlines = [PackagesAccommodationInline, PackagesMealsInline, PackagesActivitiesInline]
    list_display = ['title', 'day', 'ordering', 'is_active']
    search_fields = ['title']
    list_filter = ['is_active']

# You can also register the other models individually if needed
# admin.site.register(PackagesAccommodation)
# admin.site.register(PackagesMeals)
# admin.site.register(PackagesActivities)

from django.contrib import admin
from .models import (
    HolidaysPackages, 
    HolidaysPackagesInclusion, 
    HolidaysPackagesExclusion, 
    HolidaysPackagesNotice, 
    HolidaysPackagesDates, 
    HolidaysPackagesFaq, 
    HolidaysPackagesComments, 
    HolidaysPackagesHighlights
)

class HolidaysPackagesInclusionInline(admin.TabularInline):
    model = HolidaysPackagesInclusion
    extra = 1

class HolidaysPackagesExclusionInline(admin.TabularInline):
    model = HolidaysPackagesExclusion
    extra = 1

class HolidaysPackagesNoticeInline(admin.TabularInline):
    model = HolidaysPackagesNotice
    extra = 1

class HolidaysPackagesDatesInline(admin.TabularInline):
    model = HolidaysPackagesDates
    extra = 1

class HolidaysPackagesFaqInline(admin.TabularInline):
    model = HolidaysPackagesFaq
    extra = 1

class HolidaysPackagesCommentsInline(admin.TabularInline):
    model = HolidaysPackagesComments
    extra = 1

class HolidaysPackagesHighlightsInline(admin.TabularInline):
    model = HolidaysPackagesHighlights
    extra = 1

@admin.register(HolidaysPackages)
class HolidaysPackagesAdmin(admin.ModelAdmin):
    inlines = [
        HolidaysPackagesInclusionInline,
        HolidaysPackagesExclusionInline,
        HolidaysPackagesNoticeInline,
        HolidaysPackagesDatesInline,
        HolidaysPackagesFaqInline,
        HolidaysPackagesCommentsInline,
        HolidaysPackagesHighlightsInline
    ]
    list_display = ['name', 'category', 'price', 'is_active']
    search_fields = ['name', 'category__name']
    list_filter = ['is_active', 'category']

# Optionally, you can register the other models individually if needed
# admin.site.register(HolidaysPackagesInclusion)
# admin.site.register(HolidaysPackagesExclusion)
# admin.site.register(HolidaysPackagesNotice)
# admin.site.register(HolidaysPackagesDates)
# admin.site.register(HolidaysPackagesFaq)
# admin.site.register(HolidaysPackagesComments)
# admin.site.register(HolidaysPackagesHighlights)
