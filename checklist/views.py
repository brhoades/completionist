from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader

from checklist.forms import RunForm
from checklist.models import Checklist, ChecklistSection, ChecklistEntry, Run

from datetime import datetime


def index(request):
    checklists = Checklist.objects.order_by('-createDate')
    runs       = Run.objects.order_by('-lastUpdate', 'createDate') 
    template = loader.get_template('checklist/index.html')
    context = RequestContext(request, {'checklists': checklists, 'runs': runs })

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

    template = loader.get_template('checklist/list.html')
    return HttpResponse(template.render(context))

def newRun(request, cid):
    checklist = Checklist.objects.get(id=cid)
    if request.method == "POST":
        form = RunForm(request.POST)
        if form.is_valid():
            new_run = form.save(commit=False)
            new_run.checklist_id = checklist.id
            new_run.owner_id = 0
            new_run.save()
            return redirect('/')
        else:
            variables = RequestContext(request, {'formset': form, 'checklist': checklist.name})
            return render_to_response('checklist/run_form.html', variables)
    else:
        form = RunForm(initial={'publisher': request.user})
    variables = RequestContext(request, {'formset': form, 'game': checklist.name})
    return render_to_response('checklist/run_form.html', variables)

def run(request, rid):
    context = {}
    run = Run.objects.get(id=rid)
    list = Checklist.objects.get(id=run.checklist_id)
    sections = ChecklistSection.objects.filter(checklist_id=list.id)
    sections = sections.all()
    for section in sections:
        # FIXME: ordering probably
        entries = ChecklistEntry.objects.filter(section_id=section.id)
        section.entries = []
        for entry in entries:
            section.entries.append(entry)

    context = RequestContext(request, {'sections': sections})

    template = loader.get_template('checklist/run.html')
    return HttpResponse(template.render(context))
    

def check(request, run_id, entry_id):
    entry = ChecklistEntry.objects.get(id=entry_id)

    context = RequestContext(request, {'sections': sections})
    return HttpResponse(template.render(context))
