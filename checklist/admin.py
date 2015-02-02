from django.contrib import admin
from checklist.models import Checklist, ChecklistSection, ChecklistEntry, Run 
from adminsortable.admin import SortableTabularInline, NonSortableParentAdmin

admin.site.register( Run )

class ChecklistEntryInline( SortableTabularInline ):
    model = ChecklistEntry
    fields = [ 'name', 'description' ]
    extra = 1

class ChecklistSectionAdmin( NonSortableParentAdmin ):
    model = ChecklistSection
    fields = [ 'checklist', 'name', 'description' ]
    inlines = [ ChecklistEntryInline ]
    list_display = [ 'name', 'checklist' ]
    search_fields = [ 'name', 'checklist' ]

class ChecklistSectionInline( SortableTabularInline ):
    model = ChecklistSection
    fields = [ 'name', 'description' ]
    extra = 1

class ChecklistAdmin( NonSortableParentAdmin ):
    model = Checklist
    fields = [ 'name', 'description' ]
    inlines = [ ChecklistSectionInline ]

admin.site.register( Checklist, ChecklistAdmin )
admin.site.register( ChecklistSection, ChecklistSectionAdmin )
