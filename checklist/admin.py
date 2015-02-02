from django.contrib import admin
from checklist.models import Checklist, ChecklistSection, ChecklistEntry, Run 
from adminsortable.admin import SortableStackedInline, NonSortableParentAdmin

admin.site.register( Run )

class ChecklistEntryInline( SortableStackedInline ):
    model = ChecklistEntry

class ChecklistSectionAdmin( NonSortableParentAdmin ):
    model = ChecklistSection
    inlines = [ ChecklistEntryInline ]

class ChecklistSectionInline( SortableStackedInline ):
    model = ChecklistSection

class ChecklistAdmin( NonSortableParentAdmin ):
    model = Checklist
    inlines = [ ChecklistSectionInline ]

admin.site.register( Checklist, ChecklistAdmin )
admin.site.register( ChecklistSection, ChecklistSectionAdmin )

