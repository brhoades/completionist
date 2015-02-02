from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from checklist.models import Checklist

def index( request ):
   checklists = Checklist.objects.order_by( '-createDate' ) 
   template = loader.get_template( 'checklist/index.html' )
   context = RequestContext( request, { 'checklists': checklists } )

   return HttpResponse( template.render( context ) )
