from django.db import models
from django.conf import settings



# Create your models here.

class Country( models.Model ):
    name = models.CharField( max_length = 50 )
    FIPS104 = models.CharField( max_length = 2 )
    ISO2 = models.CharField( max_length = 2 )
    iso3 = models.CharField( max_length = 3, db_index = True, )
    ISON = models.CharField( max_length = 3 )
    internet = models.CharField( max_length = 2 )
    capital = models.CharField( max_length = 25 )
    MapReference = models.CharField( max_length = 50 )
    NationalitySingular = models.CharField( max_length = 50 )
    NationalityPlural = models.CharField( max_length = 50 )
    Currency = models.CharField( max_length = 50 )
    CurrencyCode = models.CharField( max_length = 50 )
    Population = models.CharField( max_length = 50 )
    Title = models.CharField( max_length = 50 )
    Comment = models.CharField( max_length = 255 )
    status = models.CharField( 
        max_length = 255,
        choices = settings.STATUS_CHOICES,
        default = 'active',
        db_index = True
    )

    class Meta:
        ordering = ['name', ]

    def __unicode__( self ):
        return self.name

class Region( models.Model ):
    country = models.ForeignKey( 
        Country,
        related_name = "%(app_label)s_%(class)s_related",
    )
    name = models.CharField( max_length = 50 )
    Code = models.CharField( max_length = 10 )
    ADM1Code = models.CharField( max_length = 4 )

    def __unicode__( self ):
        return self.name


class City( models.Model ):
    country = models.ForeignKey( 
        Country,
        related_name = "%(app_label)s_%(class)s_related",
    )
    region = models.ForeignKey(
        Region,
        related_name = "%(app_label)s_%(class)s_related",
    )
    name = models.CharField( max_length = 50 )
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    TimeZone = models.CharField( max_length = 10 )
    DmaId = models.IntegerField()
    County = models.CharField( max_length = 25 )
    Code = models.CharField( max_length = 4 )
    status = models.CharField( 
        max_length = 255,
        choices = settings.STATUS_CHOICES,
        default = 'active',
        db_index = True,
    )

    class Meta:
        ordering = [ 'name', ]

    def __unicode__( self ):
        return self.name
