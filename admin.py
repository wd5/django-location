from django.contrib import admin
from . models import Country, Region, City

class CountryAdmin( admin.ModelAdmin ):
    search_fields = ( 'name', )
    ordering = ['name', ]

class RegionAdmin( admin.ModelAdmin ):
    search_fields = ( 'name', )

class CityAdmin( admin.ModelAdmin ):
    search_fields = ( 'name', )
    ordering = ['country', 'name', ]

admin.site.register( Country, CountryAdmin )
admin.site.register( Region, RegionAdmin )
admin.site.register( City, CityAdmin )
