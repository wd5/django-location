from django.db import models
from django.conf import settings



# Create your models here.

class Country( models.Model ):
    name = models.CharField( max_length = 50 )#     varchar(50)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    FIPS104 = models.CharField( max_length = 2 )#    3     FIPS104     varchar(2)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    ISO2 = models.CharField( max_length = 2 )#    4     ISO2     varchar(2)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    iso3 = models.CharField( max_length = 3, db_index = True, )#    5     iso3     varchar(3)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    ISON = models.CharField( max_length = 3 )#    6     ISON     varchar(4)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    internet = models.CharField( max_length = 2 )#    7     internet     varchar(2)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    capital = models.CharField( max_length = 25 )#    8     capital     varchar(25)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    MapReference = models.CharField( max_length = 50 )#    9     MapReference     varchar(50)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    NationalitySingular = models.CharField( max_length = 50 )#    10     NationalitySingular     varchar(35)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    NationalityPlural = models.CharField( max_length = 50 )#    11     NationalityPlural     varchar(35)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    Currency = models.CharField( max_length = 50 )#    12     Currency     varchar(30)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    CurrencyCode = models.CharField( max_length = 50 )#    13     CurrencyCode     varchar(3)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    Population = models.CharField( max_length = 50 )#    14     Population     bigint(20)             Yes     NULL         Change Change     Drop Drop     More Show more actions
    Title = models.CharField( max_length = 50 )#    15     Title     varchar(50)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    Comment = models.CharField( max_length = 255 )#    16     Comment     varchar(255)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    status = models.CharField( max_length = 255, choices = settings.STATUS_CHOICES, default = 'active', db_index = True )#    17     status     enum('active', ' inactive')     utf8_general_ci         Yes     active

    class Meta:
        ordering = ['name', ]

    def __unicode__( self ):
        return self.name

class Region( models.Model ):
    country = models.ForeignKey( Country )#   smallint(6)             Yes     NULL         Change Change     Drop Drop     More Show more actions
    name = models.CharField( max_length = 50 )#    varchar(45)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    Code = models.CharField( max_length = 10 )#   varchar(8)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    ADM1Code = models.CharField( max_length = 4 )#     char(4)     utf8_general_ci         Yes

    def __unicode__( self ):
        return self.name


class City( models.Model ):
    country = models.ForeignKey( Country, blank = True, null = True, default = 1, )#     smallint(6)         UNSIGNED     Yes     NULL         Change Change     Drop Drop     More Show more actions
    region = models.ForeignKey( Region, blank = True, null = True, )#   smallint(6)             Yes     NULL         Change Change     Drop Drop     More Show more actions
    name = models.CharField( max_length = 50 )#     varchar(45)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    Latitude = models.FloatField()#     float             Yes     NULL         Change Change     Drop Drop     More Show more actions
    Longitude = models.FloatField()#   float             Yes     NULL         Change Change     Drop Drop     More Show more actions
    TimeZone = models.CharField( max_length = 10 )#     varchar(10)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    DmaId = models.IntegerField()#   smallint(6)             Yes     NULL         Change Change     Drop Drop     More Show more actions
    County = models.CharField( max_length = 25 )#    varchar(25)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    Code = models.CharField( max_length = 4 )#   varchar(4)     utf8_general_ci         Yes     NULL         Change Change     Drop Drop     More Show more actions
    status = models.CharField( max_length = 255, choices = settings.STATUS_CHOICES, default = 'active', db_index = True, )#    17     status     enum('active', ' inactive')     utf8_general_ci         Yes     active

    class Meta:
        ordering = [ 'name', ]

    def __unicode__( self ):
        return self.name
