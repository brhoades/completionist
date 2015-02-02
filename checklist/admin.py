from django.contrib import admin
from checklist.models import Checklist, ChecklistSection, ChecklistEntry, Run 
# Register your models here.

admin.site.register( Checklist )
admin.site.register( ChecklistSection )
admin.site.register( ChecklistEntry )
admin.site.register( Run )
