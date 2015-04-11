from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from checklist.models import Checklist, ChecklistSection, ChecklistEntry


def index(request):
    checklists = Checklist.objects.order_by('-createDate')
    template = loader.get_template('checklist/index.html')
    context = RequestContext(request, {'checklists': checklists})

    return HttpResponse(template.render(context))


def checklist(request, cid):
    context = {}
    list = Checklist.objects.get(id=cid)
    sections = ChecklistSection.objects.filter(checklist_id=cid)
    sections = sections.all()
    for section in sections:
        # FIXME: ordering probably
        entries = ChecklistEntry.objects.filter(section_id=section.id)
        section.entries = []
        for entry in entries:
            section.entries.append(entry)

    context = RequestContext(request, {'sections': sections})

    print(sections)

    template = loader.get_template('checklist/list.html')
    return HttpResponse(template.render(context))


def check(request, run_id, entry_id):
    entry = ChecklistEntry.objects.get(id=entry_id)

    context = RequestContext(request, {'sections': sections})
    return HttpResponse(template.render(context))
