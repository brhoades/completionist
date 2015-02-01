from django.db import models
from django.contrib.auth.models import User

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

class ChecklistEntry( models.Model ):
    section = models.ForeignKey( ChecklistSection )

    position = models.PositiveIntegerField( db_index=True, blank=False, null=False )

    name = models.CharField( max_length=50 )
    description = models.TextField( )
    image = models.ImageField( )

    class Meta( object ):
        ordering = ['position']

class Run( models.Model ):
    createDate = models.DateTimeField( auto_now_add=True )
    lastUpdate = models.DateTimeField( auto_now=True )

    name = models.CharField( max_length=100 )
    description = models.TextField( )

    checklist = models.ForeignKey( Checklist )
    owner = models.ForeignKey( User )

class RunProgress( models.Model ):
    run = models.ForeignKey( Run ) 
    entry = models.ForeignKey( ChecklistEntry )
    completed = models.DateTimeField( auto_now_add=True )

    # If it is later unchecked and rechecked.
    checked = models.BooleanField( default=True )
    # For items if you aren't sure you completed.
    unsure  = models.BooleanField( default=False )
