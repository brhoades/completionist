from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from checklist.forms import RunForm
from checklist.models import Checklist, ChecklistSection, ChecklistEntry, Run, RunProgress

from datetime import datetime
import json


def index(request):
    runs = None
    checklists = Checklist.objects.order_by('-createDate')
    if request.user.is_authenticated():
        runs = Run.objects.filter(owner=request.user.id).order_by('-lastUpdate', 'createDate') 
    else:
        runs = Run.objects.order_by('-lastUpdate', 'createDate') 
        for run in runs:
            run.owner = User.objects.get(id=run.owner_id)
    template = loader.get_template('checklist/index.html')
    context = RequestContext(request, {'checklists': checklists, 'runs': runs, 'user': request.user })

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

@login_required
def newRun(request, cid):
    checklist = Checklist.objects.get(id=cid)
    if request.method == "POST":
        form = RunForm(request.POST)
        if form.is_valid():
            new_run = form.save(commit=False)
            new_run.checklist_id = checklist.id
            new_run.owner_id = request.user.id
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

    context = RequestContext(request, {'sections': sections, 'rid': rid})

    template = loader.get_template('checklist/run.html')
    return HttpResponse(template.render(context))
    
@login_required
def check(request, rid, eid):
    """
       Entry is checked via AJAX
    """
    prog = None
    run = Run.objects.get(id=rid)
    message = ""
    if request.user.id != run.owner_id:
        message = "You do not own this list." 

    if message == "":
        try:
            prog = RunProgress.objects.get(run_id=rid, entry_id=eid)
            prog.checked = not prog.checked
        except:
            prog = RunProgress.objects.create(run_id=rid, entry_id=eid) 

        prog.save( )

    context = {'state': prog.checked, 'message': message}
    return HttpResponse(json.dumps(context))
