from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from checklist.models import Checklist, ChecklistSection, ChecklistEntry

def index( request ):
   checklists = Checklist.objects.order_by( '-createDate' ) 
   template = loader.get_template( 'checklist/index.html' )
   context = RequestContext( request, { 'checklists': checklists } )

   return HttpResponse( template.render( context ) )

def checklist( request, cid ):
    context = { }
    list = Checklist.objects.get( id=cid )
    sections = ChecklistSection.objects.filter( checklist_id=cid )
    for section in sections.all( ):
        #FIXME: ordering probably
        entries = ChecklistEntry.objects.filter( section_id=section.id )
        context[section.name] = [ ]
        for entry in entries:
            context[section.name].append( entry.name )
    
    context = RequestContext( request, { 'checklist': context } )

    template = loader.get_template( 'checklist/list.html' )
    return HttpResponse( template.render( context ) )
