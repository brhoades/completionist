from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from checklist.forms import RunForm
from checklist.models import Checklist, ChecklistSection, ChecklistEntry, Run

from datetime import datetime


def index(request):
    runs = None
    checklists = Checklist.objects.order_by('-createDate')
    if request.user.is_authenticated():
        runs = Run.get(owner=request.user.id).order_by('-lastUpdate', 'createDate') 
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
    
@login_required
def check(request, run_id, entry_id):
    entry = ChecklistEntry.objects.get(id=entry_id)

    context = RequestContext(request, {'sections': sections})
    return HttpResponse(template.render(context))


"""

AUTHENTICATION


def authuser(request):
    if 'username' in request.post and 'password' in request.post:
        username = request.post['username']
        password = request.post['password']
        user = authenticate(username, password)
        context = None
        template = loader.get_template('checklist/login.html')
        return HttpResponse(template.render(context))

        if user is not None:
            if user.is_active: #GOOD
                login(request, user)
                return redirect('/')
            else: #INACTIVE
                context = RequestContext(request, {'message': "Account is disabled or inactive" })
        else:
            context = RequestContext(request, {'message': "Invalid credentials provided" })

        return HttpResponse(template.render(context))
"""
