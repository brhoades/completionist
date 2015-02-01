from django.db import models

class Checklist( models.Model ):
    createDate = models.DateTimeField( auto_now_add=True )
    lastUpdate = models.DateTimeField( auto_now=True )

    name = models.CharField( max_length=100 )
    description = models.TextField( )
    image = models.ImageField( )

class ChecklistSection( models.Model ):
    checklist = models.ForeignKey( Checklist )
    position = models.PositiveIntegerField( db_index=True, blank=False, null=False )

    name = models.CharField( max_length=100 )
    description = models.TextField( )
    image = models.ImageField( )

    class Meta( object ):
        ordering = ['position']

class ChecklistEntries( models.Model ):
    section = models.ForeignKey( ChecklistSection )

    position = models.PositiveIntegerField( db_index=True, blank=False, null=False )

    name = models.CharField( max_length=50 )
    description = models.TextField( )
    image = models.ImageField( )

    class Meta( object ):
        ordering = ['position']
