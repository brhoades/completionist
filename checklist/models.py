from django.db import models
from django.contrib.auth.models import User
from adminsortable.models import Sortable


class Checklist( models.Model ):
    createDate = models.DateTimeField( auto_now_add=True )
    lastUpdate = models.DateTimeField( auto_now=True )

    name = models.CharField( max_length=100 )
    description = models.TextField( blank=True )
    image = models.ImageField( blank=True )

    def __str__( self ):
        return self.name

class ChecklistSection( Sortable ):
    class Meta( Sortable.Meta ):
        pass

    checklist = models.ForeignKey( Checklist )

    name = models.CharField( max_length=100 )
    description = models.TextField( blank=True )
    image = models.ImageField( blank=True )

    def __str__( self ):
        return self.name

class ChecklistEntry( Sortable ):
    class Meta( Sortable.Meta ):
        pass
    section = models.ForeignKey( ChecklistSection )

    name = models.CharField( max_length=50 )
    description = models.TextField( blank=True )
    image = models.ImageField( blank=True )

    def __str__( self ):
        return self.name

class Run( models.Model ):
    createDate = models.DateTimeField( auto_now_add=True )
    endDate =    models.DateTimeField( blank=True )
    lastUpdate = models.DateTimeField( auto_now=True )

    name = models.CharField( max_length=100 )
    description = models.TextField( blank=True )

    checklist = models.ForeignKey( Checklist )
    owner = models.ForeignKey( User )

    def __str__( self ):
        return self.name

class RunProgress( models.Model ):
    run = models.ForeignKey( Run ) 
    entry = models.ForeignKey( ChecklistEntry )
    completed = models.DateTimeField( auto_now_add=True )

    # If it is later unchecked and rechecked.
    checked = models.BooleanField( default=True )
    # For items if you aren't sure you completed.
    unsure  = models.BooleanField( default=False )
